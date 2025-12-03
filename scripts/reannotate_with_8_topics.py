"""
Script to re-annotate data with the new 8 topics structure.
Reads from raw reddit_posts.csv and assigns topics based on codebook definitions.

Run from project root: python scripts/reannotate_with_8_topics.py
"""
import sys
from pathlib import Path
import pandas as pd
import re

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path, save_dataframe


def identify_movie(row):
    """Identify which movie a post is about."""
    title = str(row.get('title', '')).lower()
    text = str(row.get('selftext', '')).lower()[:500]
    combined = title + ' ' + text
    
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']):
        return 'Superman'
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        return 'Fantastic Four'
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        return 'Jurassic World'
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        return 'Smurfs'
    return 'Other'


def classify_topic(row):
    """Classify a post into one of the 8 topics based on codebook."""
    title = str(row.get('title', '')).lower()
    text = str(row.get('selftext', '')).lower()
    combined = title + ' ' + text[:2000]  # Use first 2000 chars for efficiency
    
    # Check for box office keywords first (most common)
    box_office_keywords = ['box office', 'gross', 'million', 'billion', 'earned', 'made', 
                          'debuted', 'opened', 'weekend', 'recap', 'total', 'domestic', 
                          'worldwide', 'overseas', 'international', 'revenue', 'ticket', 
                          'admission', 'forecast', 'projection', 'tracking', 'presale',
                          'drop', 'decline', 'fell', 'reached', 'crossed', 'stands at']
    
    has_box_office = any(kw in combined for kw in box_office_keywords)
    
    # If box office related, determine which movie
    if has_box_office:
        movie = identify_movie(row)
        if movie == 'Superman':
            return '1a'
        elif movie == 'Fantastic Four':
            return '1b'
        else:  # Jurassic World, Smurfs, or Other
            return '1c'
    
    # Check for Audience Reception and Scores
    audience_keywords = ['audience score', 'cinemascore', 'rottentomatoes', 'rotten tomatoes',
                        'rt score', 'posttrak', 'recommend', 'demographic', 'cgv', 'megabox',
                        'audience reception', 'audience rating', 'viewer score', 'user score']
    if any(kw in combined for kw in audience_keywords):
        return '2'
    
    # Check for Marketing, Franchise Strategy and Distribution
    marketing_keywords = ['marketing', 'trailer', 'tv spot', 'release date', 'release timing',
                         'pvod', 'streaming', 'theatrical', 'slate', 'franchise', 'universe',
                         'dcu', 'mcu', 'greenlight', 'cancellation', 'sequel', 'prequel',
                         'reboot', 'remake', 'distribution', 'platform', 'window']
    if any(kw in combined for kw in marketing_keywords):
        return '3'
    
    # Check for Film Quality, Creative Content and Characters
    quality_keywords = ['quality', 'tone', 'direction', 'director', 'scene', 'character',
                       'portrayal', 'acting', 'performance', 'cinematography', 'editing',
                       'storytelling', 'script', 'writing', 'style', 'visual', 'soundtrack',
                       'score', 'music', 'better than', 'worse than', 'compared to',
                       'review', 'critic', 'opinion', 'thoughts on', 'what did you think']
    if any(kw in combined for kw in quality_keywords) and not has_box_office:
        return '4'
    
    # Check for Fandom, Rankings and Community Meta Discussion
    fandom_keywords = ['ranking', 'top 10', 'best', 'worst', 'favorite', 'favourite',
                      'megathread', 'discussion thread', 'official discussion', 'ama',
                      'ask me anything', 'viewing plan', 'going to watch', 'theatre',
                      'screening', 'worried', 'prediction', 'expectation', 'fan',
                      'community', 'meta', 'poll', 'vote']
    if any(kw in combined for kw in fandom_keywords):
        return '5'
    
    # Check for General News
    news_keywords = ['dies', 'death', 'cast', 'casting', 'announced', 'confirmed',
                    'report', 'news', 'update', 'breaking', 'exclusive', 'rumor',
                    'rumour', 'leak', 'sources say']
    if any(kw in combined for kw in news_keywords) and not has_box_office:
        return '6'
    
    # Default to General News and Other
    return '6'


def reannotate_data():
    """Re-annotate data with new 8 topics."""
    # Load raw data
    print("Loading raw reddit_posts.csv...")
    df = pd.read_csv(get_data_path('raw') / 'reddit_posts.csv')
    
    print(f"Total posts: {len(df)}")
    print()
    
    # Classify topics
    print("Classifying posts into 8 topics...")
    df['topic'] = df.apply(classify_topic, axis=1)
    
    # Count by topic
    print("\nClassification results:")
    print("-" * 60)
    topic_counts = df['topic'].value_counts().sort_index()
    topic_names = {
        '1a': 'Box Office - Superman',
        '1b': 'Box Office - Fantastic Four',
        '1c': 'Box Office - Jurassic World and Other',
        '2': 'Audience Reception and Scores',
        '3': 'Marketing, Franchise Strategy and Distribution',
        '4': 'Film Quality, Creative Content and Characters',
        '5': 'Fandom, Rankings and Community Meta Discussion',
        '6': 'General News and Other'
    }
    
    for topic_code in ['1a', '1b', '1c', '2', '3', '4', '5', '6']:
        count = topic_counts.get(topic_code, 0)
        pct = (count / len(df) * 100) if len(df) > 0 else 0
        name = topic_names.get(topic_code, 'Unknown')
        print(f"  {topic_code}. {name:50s}: {count:4d} posts ({pct:5.1f}%)")
    
    # Save annotated data
    output_path = save_dataframe(df, 'reddit_posts_annotated_8topics.csv', subfolder='processed')
    print(f"\n✓ Annotated data saved to: {output_path}")
    print(f"\nThe file includes:")
    print(f"  - All original columns from reddit_posts.csv")
    print(f"  - New 'topic' column with 8 topic codes (1a, 1b, 1c, 2, 3, 4, 5, 6)")
    print()
    print("Note: This is automatic classification. You may want to review and")
    print("      manually adjust some classifications for accuracy.")


if __name__ == "__main__":
    reannotate_data()

