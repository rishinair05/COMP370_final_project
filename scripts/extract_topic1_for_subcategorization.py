"""
Script to extract Topic 1 (Box Office and Financial Performance) posts
into a separate CSV file for subcategorization.

Run from project root: python scripts/extract_topic1_for_subcategorization.py
"""
import sys
from pathlib import Path
import pandas as pd

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.data_utils import get_data_path


def extract_topic1():
    """Extract Topic 1 posts to a separate CSV for subcategorization."""
    # Load annotated data
    print("Loading annotated_data.csv...")
    data_path = get_data_path('processed') / 'annotated_data.csv'
    df = pd.read_csv(data_path)
    
    # Filter for Topic 1 only
    topic1_df = df[df['topics'] == 1.0].copy()
    
    print(f"Total posts in dataset: {len(df)}")
    print(f"Topic 1 posts found: {len(topic1_df)}")
    
    # Add a new column for subcategory (empty for now)
    topic1_df['subcategory'] = ''
    
    # Reorder columns to put subcategory near topics
    cols = ['id', 'title', 'selftext', 'subreddit', 'created_utc', 'author', 
            'permalink', 'url', 'score', 'topics', 'subcategory', 'Ai_topic']
    topic1_df = topic1_df[cols]
    
    # Reset index for easier viewing
    topic1_df = topic1_df.reset_index(drop=True)
    
    # Save to new CSV file
    output_path = get_data_path('processed') / 'topic1_for_subcategorization.csv'
    topic1_df.to_csv(output_path, index=False)
    
    print(f"\nTopic 1 posts saved to: {output_path}")
    print(f"\nThe file includes:")
    print(f"  - All original columns")
    print(f"  - New 'subcategory' column (empty, ready for you to fill in)")
    print(f"\nYou can now:")
    print(f"  1. Open the CSV file")
    print(f"  2. Review the posts")
    print(f"  3. Assign subcategories (e.g., '1a', '1b' or descriptive names)")
    print(f"  4. Save your subcategorization")
    
    # Show some sample posts
    print(f"\nSample of first 3 posts:")
    print("-" * 80)
    for idx, row in topic1_df.head(3).iterrows():
        print(f"\nPost {idx + 1}:")
        print(f"  ID: {row['id']}")
        print(f"  Title: {str(row['title'])[:80]}...")
        print(f"  Subreddit: {row['subreddit']}")


if __name__ == "__main__":
    extract_topic1()

