"""
Script to analyze topic distribution - Question 1:
What aspect of the movie was the focus (topic) of the article?

Analyzes which topics are most common for each movie and overall.

Run from project root: python scripts/analyze_topic_distribution.py
"""
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path


def identify_movie(row):
    """Identify which movie(s) a post is about based on title and text."""
    title = str(row.get('title', '')).lower()
    selftext = str(row.get('selftext', '')).lower()
    combined = f"{title} {selftext}".lower()
    
    movies = []
    
    # Keywords for each movie
    superman_keywords = ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']
    jurassic_keywords = ['jurassic', 'jurassic world', 'rebirth']
    fantastic_keywords = ['fantastic four', 'fantastic 4', 'ff4', 'first steps']
    smurfs_keywords = ['smurf', 'smurfs']
    
    if any(kw in combined for kw in superman_keywords):
        movies.append('Superman')
    if any(kw in combined for kw in jurassic_keywords):
        movies.append('Jurassic World')
    if any(kw in combined for kw in fantastic_keywords):
        movies.append('Fantastic Four')
    if any(kw in combined for kw in smurfs_keywords):
        movies.append('Smurfs')
    
    return movies if movies else ['Other']


def analyze_topic_distribution():
    """Analyze topic distribution across movies."""
    # Load annotated data
    print("Loading final_dataset.xlsx...")
    data_path = get_data_path('processed') / 'final_dataset.xlsx'
    df = pd.read_excel(data_path)
    
    # If Excel file doesn't have headers, assign them
    if 'topic' not in df.columns and 'topics' not in df.columns:
        if len(df.columns) == 10:
            df.columns = ['id', 'title', 'selftext', 'subreddit', 'created_utc', 
                         'author', 'permalink', 'url', 'score', 'topic']
    
    # Filter to posts with topics (check for both 'topic' and 'topics' column names)
    topic_col = 'topic' if 'topic' in df.columns else 'topics'
    df = df[df[topic_col].notna()].copy()
    
    # Convert topic column to string to handle mixed types
    df[topic_col] = df[topic_col].astype(str)
    
    print(f"Total posts with topics: {len(df)}")
    print()
    
    # Identify movies
    print("Identifying movies in posts...")
    df['movies'] = df.apply(identify_movie, axis=1)
    
    # Expand rows where a post mentions multiple movies
    expanded_rows = []
    for _, row in df.iterrows():
        for movie in row['movies']:
            new_row = row.copy()
            new_row['movie'] = movie
            expanded_rows.append(new_row)
    
    df_expanded = pd.DataFrame(expanded_rows)
    
    # Topic names (8 topics structure: 1a, 1b, 1c, 2, 3, 4, 5, 6)
    topic_names = {
        '1a': "Box Office - Superman",
        '1b': "Box Office - Fantastic Four",
        '1c': "Box Office - Jurassic World and Other Movies",
        '2': "Audience Reception and Scores",
        '3': "Marketing, Franchise Strategy and Distribution",
        '4': "Film Quality, Creative Content and Characters",
        '5': "Fandom, Rankings and Community Meta Discussion",
        '6': "General News and Other"
    }
    
    # Map topic codes to topic names
    df_expanded['topic_name'] = df_expanded[topic_col].map(topic_names)
    
    print("\n" + "=" * 80)
    print("TOPIC DISTRIBUTION ANALYSIS")
    print("=" * 80)
    
    # Overall topic distribution
    print("\n1. OVERALL TOPIC DISTRIBUTION (All Movies Combined)")
    print("-" * 80)
    overall = df_expanded['topic_name'].value_counts().sort_index()
    total = len(df_expanded)
    for topic_name in sorted(topic_names.values()):
        count = overall.get(topic_name, 0)
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {topic_name:50s}: {count:4d} posts ({pct:5.1f}%)")
    
    # Topic distribution by movie
    print("\n\n2. TOPIC DISTRIBUTION BY MOVIE")
    print("-" * 80)
    
    movies = ['Superman', 'Jurassic World', 'Fantastic Four', 'Smurfs', 'Other']
    
    for movie in movies:
        movie_df = df_expanded[df_expanded['movie'] == movie]
        if len(movie_df) == 0:
            continue
        
        print(f"\n{movie}:")
        print(f"  Total posts: {len(movie_df)}")
        
        topic_counts = movie_df['topic_name'].value_counts().sort_index()
        for topic_name in sorted(topic_names.values()):
            count = topic_counts.get(topic_name, 0)
            pct = (count / len(movie_df) * 100) if len(movie_df) > 0 else 0
            if count > 0:
                print(f"    {topic_name:50s}: {count:4d} ({pct:5.1f}%)")
    
    # Focus on Superman (main research question)
    print("\n\n3. SUPERMAN-SPECIFIC ANALYSIS")
    print("-" * 80)
    superman_df = df_expanded[df_expanded['movie'] == 'Superman']
    
    if len(superman_df) > 0:
        print(f"\nTotal Superman posts: {len(superman_df)}")
        print("\nTopic distribution for Superman posts:")
        
        superman_topics = superman_df['topic_name'].value_counts().sort_index()
        for topic_name in sorted(topic_names.values()):
            count = superman_topics.get(topic_name, 0)
            pct = (count / len(superman_df) * 100) if len(superman_df) > 0 else 0
            if count > 0:
                print(f"  {topic_name:50s}: {count:4d} posts ({pct:5.1f}%)")
        
        # Top 3 topics for Superman
        print("\nTop 3 most discussed aspects of Superman:")
        top3 = superman_df['topic_name'].value_counts().head(3)
        for i, (topic, count) in enumerate(top3.items(), 1):
            pct = (count / len(superman_df) * 100)
            print(f"  {i}. {topic} ({count} posts, {pct:.1f}%)")
    
    # Save detailed results
    print("\n\n4. SAVING RESULTS")
    print("-" * 80)
    
    # Save overall topic distribution
    # Sort topics: 1a, 1b, 1c, 2, 3, 4, 5, 6
    topic_order = ['1a', '1b', '1c', '2', '3', '4', '5', '6']
    overall_output = get_data_path('processed') / 'topic_distribution_overall.csv'
    overall_df = pd.DataFrame({
        'topic_id': topic_order,
        'topic_name': [topic_names[k] for k in topic_order],
        'count': [overall.get(topic_names[k], 0) for k in topic_order],
        'percentage': [(overall.get(topic_names[k], 0) / total * 100) if total > 0 else 0 
                      for k in topic_order]
    })
    overall_df.to_csv(overall_output, index=False)
    print(f"Overall topic distribution saved to: {overall_output}")
    
    # Save topic distribution by movie
    movie_topic_output = get_data_path('processed') / 'topic_distribution_by_movie.csv'
    movie_topic_data = []
    for movie in movies:
        movie_df = df_expanded[df_expanded['movie'] == movie]
        if len(movie_df) == 0:
            continue
        for topic_id, topic_name in topic_names.items():
            count = len(movie_df[movie_df[topic_col] == topic_id])
            pct = (count / len(movie_df) * 100) if len(movie_df) > 0 else 0
            movie_topic_data.append({
                'movie': movie,
                'topic_id': topic_id,
                'topic_name': topic_name,
                'count': count,
                'percentage': pct
            })
    
    movie_topic_df = pd.DataFrame(movie_topic_data)
    movie_topic_df.to_csv(movie_topic_output, index=False)
    print(f"Topic distribution by movie saved to: {movie_topic_output}")
    
    # Save text summary
    summary_output = get_data_path('processed') / 'topic_distribution_summary.txt'
    with open(summary_output, 'w', encoding='utf-8') as f:
        f.write("TOPIC DISTRIBUTION ANALYSIS - SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("RESEARCH QUESTION 1:\n")
        f.write("What aspect of the movie was the focus (topic) of the article?\n\n")
        
        f.write("OVERALL TOPIC DISTRIBUTION:\n")
        f.write("-" * 80 + "\n")
        for topic_name in sorted(topic_names.values()):
            count = overall.get(topic_name, 0)
            pct = (count / total * 100) if total > 0 else 0
            f.write(f"{topic_name:50s}: {count:4d} posts ({pct:5.1f}%)\n")
        
        f.write("\n\nSUPERMAN-SPECIFIC TOPIC DISTRIBUTION:\n")
        f.write("-" * 80 + "\n")
        if len(superman_df) > 0:
            f.write(f"Total Superman posts: {len(superman_df)}\n\n")
            for topic_name in sorted(topic_names.values()):
                count = superman_topics.get(topic_name, 0)
                pct = (count / len(superman_df) * 100) if len(superman_df) > 0 else 0
                if count > 0:
                    f.write(f"{topic_name:50s}: {count:4d} posts ({pct:5.1f}%)\n")
            
            f.write("\nTop 3 most discussed aspects of Superman:\n")
            for i, (topic, count) in enumerate(top3.items(), 1):
                pct = (count / len(superman_df) * 100)
                f.write(f"  {i}. {topic} ({count} posts, {pct:.1f}%)\n")
    
    print(f"Summary saved to: {summary_output}")
    print("\n" + "=" * 80)
    print("Analysis complete!")


if __name__ == "__main__":
    analyze_topic_distribution()

