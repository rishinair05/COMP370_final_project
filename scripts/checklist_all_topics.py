"""
Script to create a checklist of all topics with their distributions.
Shows what we have and what might need subcategorization.

Run from project root: python scripts/checklist_all_topics.py
"""
import sys
from pathlib import Path
import pandas as pd

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path


def identify_movie(row):
    """Identify which movie a post is about."""
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:500]
    combined = title + ' ' + text
    
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']):
        return 'Superman'
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        return 'Jurassic World'
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        return 'Fantastic Four'
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        return 'Smurfs'
    return 'Other'


def checklist_all_topics():
    """Create a checklist of all topics."""
    # Load annotated data
    print("Loading annotated_data.csv...")
    data_path = get_data_path('processed') / 'annotated_data.csv'
    df = pd.read_csv(data_path)
    
    # Filter to posts with topics
    df = df[df['topics'].notna()].copy()
    df['topics'] = df['topics'].astype(int)
    
    # Identify movies
    df['movie'] = df.apply(identify_movie, axis=1)
    
    # Topic names
    topic_names = {
        1: "Box Office and Financial Performance",
        2: "Audience Reception and Scores",
        3: "Marketing, Franchise Strategy and Distribution",
        4: "Film Quality, Creative Content and Characters",
        5: "Fandom, Rankings and Community Meta Discussion",
        6: "General News",
        7: "Other"
    }
    
    print("=" * 80)
    print("COMPLETE TOPIC CHECKLIST")
    print("=" * 80)
    print()
    
    total = len(df)
    
    for topic_id in sorted(df['topics'].unique()):
        topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
        topic_df = df[df['topics'] == topic_id]
        count = len(topic_df)
        pct = (count / total * 100) if total > 0 else 0
        
        print(f"TOPIC {topic_id}: {topic_name}")
        print("-" * 80)
        print(f"  Total posts: {count} ({pct:.1f}% of all posts)")
        print()
        
        # Show distribution by movie
        movie_counts = topic_df['movie'].value_counts()
        print("  Distribution by movie:")
        for movie in ['Superman', 'Jurassic World', 'Fantastic Four', 'Smurfs', 'Other']:
            movie_count = movie_counts.get(movie, 0)
            if movie_count > 0:
                movie_pct = (movie_count / count * 100) if count > 0 else 0
                print(f"    {movie:20s}: {movie_count:4d} posts ({movie_pct:5.1f}%)")
        print()
        
        # Show distribution by subreddit
        subreddit_counts = topic_df['subreddit'].value_counts()
        print("  Distribution by subreddit:")
        for subreddit, sub_count in subreddit_counts.items():
            sub_pct = (sub_count / count * 100) if count > 0 else 0
            print(f"    r/{subreddit:15s}: {sub_count:4d} posts ({sub_pct:5.1f}%)")
        print()
        
        # Suggest if subcategorization might be needed
        if count > 100:
            print(f"  ⚠️  LARGE CATEGORY - Consider subcategorization")
        elif count < 30:
            print(f"  ✓ Small category - Probably fine as is")
        else:
            print(f"  → Medium category - Subcategorization optional")
        print()
        print()
    
    print("=" * 80)
    print("SUMMARY & RECOMMENDATIONS")
    print("=" * 80)
    print()
    print("Topics that might need subcategorization:")
    print()
    
    for topic_id in sorted(df['topics'].unique()):
        topic_name = topic_names.get(topic_id, f"Topic {topic_id}")
        topic_df = df[df['topics'] == topic_id]
        count = len(topic_df)
        
        if count > 100:
            print(f"  ✓ Topic {topic_id} ({topic_name}): {count} posts")
            print(f"    → Already being considered for subcategorization")
            print()
    
    print("=" * 80)
    print("RESEARCH QUESTIONS REMINDER")
    print("=" * 80)
    print()
    print("Question 1: What aspect of the movie was the focus (topic)?")
    print("  → All 7 topics help answer this")
    print()
    print("Question 2: How much coverage relative to other movies?")
    print("  → Need to compare coverage across movies within each topic")
    print("  → Topic 1 (Box Office) is largest, so subcategorizing by movie helps")
    print()
    print("=" * 80)


if __name__ == "__main__":
    checklist_all_topics()

