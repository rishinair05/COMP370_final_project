"""
Helper script to view open coding progress and statistics.

Run from project root: 
  python scripts/view_coding_progress.py          # Show progress
  python scripts/view_coding_progress.py view 5   # View post at index 5
"""
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pandas as pd
from src.data_utils import get_data_path


def view_progress():
    """Display coding progress and statistics."""
    coding_file = get_data_path('processed') / 'open_coding_sample.csv'
    
    try:
        df = pd.read_csv(coding_file)
    except FileNotFoundError:
        print(f"Error: {coding_file} not found.")
        print("Run scripts/prepare_open_coding.py first to create the coding file.")
        return
    
    total = len(df)
    # Handle both NaN and empty string cases
    coded = df['topic'].notna() & (df['topic'].astype(str).str.strip() != '') & (df['topic'].astype(str) != 'nan')
    coded_count = coded.sum()
    uncoded_count = total - coded_count
    
    print("=" * 60)
    print("OPEN CODING PROGRESS")
    print("=" * 60)
    print(f"Total posts: {total}")
    print(f"Coded: {coded_count} ({coded_count/total*100:.1f}%)")
    print(f"Remaining: {uncoded_count} ({uncoded_count/total*100:.1f}%)")
    print()
    
    if coded_count > 0:
        # Show topic distribution
        topics = df[coded]['topic'].value_counts()
        print("Current Topics (and counts):")
        print("-" * 60)
        for topic, count in topics.items():
            print(f"  {topic}: {count} posts")
        print()
        
        # Show some uncoded posts
        if uncoded_count > 0:
            uncoded = df[~coded]
            print(f"Next {min(5, uncoded_count)} uncoded posts to work on:")
            print("-" * 60)
            for idx, row in uncoded.head(5).iterrows():
                print(f"\n[{idx + 1}] ID: {row['id']}")
                print(f"    Title: {row['title'][:80]}...")
                print(f"    Subreddit: {row['subreddit']}")
    else:
        print("No posts coded yet. Start coding in the 'topic' column!")
    
    print("\n" + "=" * 60)


def view_post(post_id=None, index=None):
    """View a specific post in detail."""
    coding_file = get_data_path('processed') / 'open_coding_sample.csv'
    
    try:
        df = pd.read_csv(coding_file)
    except FileNotFoundError:
        print(f"Error: {coding_file} not found.")
        return
    
    if post_id:
        post = df[df['id'] == post_id]
    elif index is not None:
        post = df.iloc[index:index+1]
    else:
        print("Please provide either post_id or index")
        return
    
    if post.empty:
        print("Post not found")
        return
    
    row = post.iloc[0]
    print("=" * 60)
    print(f"POST ID: {row['id']}")
    print("=" * 60)
    print(f"Subreddit: r/{row['subreddit']}")
    print(f"Current Topic: {row['topic'] if pd.notna(row['topic']) else '[NOT CODED]'}")
    print()
    print("TEXT FOR CODING:")
    print("-" * 60)
    print(row['text_for_coding'])
    print("-" * 60)
    if pd.notna(row['notes']) and row['notes'].strip():
        print(f"\nNotes: {row['notes']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == 'view' and len(sys.argv) > 2:
            # View specific post by index
            try:
                index = int(sys.argv[2])
                view_post(index=index)
            except ValueError:
                view_post(post_id=sys.argv[2])
        else:
            print("Usage:")
            print("  python scripts/view_coding_progress.py          # Show progress")
            print("  python scripts/view_coding_progress.py view 5   # View post at index 5")
    else:
        view_progress()

