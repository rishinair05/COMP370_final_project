"""
Script to prepare 200 posts for open coding.
Extracts title and opening text (first 500 characters) from posts.

Run from project root: python scripts/prepare_open_coding.py
"""
import sys
from pathlib import Path

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

import pandas as pd
from src.data_utils import load_reddit_posts, save_dataframe
from src.text_processing import get_opening_text, prepare_text_for_coding

def main():
    # Load the full dataset
    print("Loading reddit_posts.csv...")
    df = load_reddit_posts('reddit_posts.csv', subfolder='raw')

    print(f"Total posts available: {len(df)}")

    # Sample 200 posts randomly
    n_samples = min(200, len(df))
    sample_df = df.sample(n=n_samples, random_state=42).copy()

    # Extract title and opening text
    sample_df['opening_text'] = sample_df['selftext'].apply(get_opening_text)
    sample_df['text_for_coding'] = sample_df.apply(
        lambda row: prepare_text_for_coding(row['title'], row['opening_text']), 
        axis=1
    )

    # Create coding dataframe with essential columns
    coding_df = pd.DataFrame({
        'id': sample_df['id'],
        'title': sample_df['title'],
        'opening_text': sample_df['opening_text'],
        'text_for_coding': sample_df['text_for_coding'],
        'subreddit': sample_df['subreddit'],
        'topic': '',  # Empty column for manual coding
        'notes': '',  # Optional notes column
        'original_index': sample_df.index  # To track back to original
    })

    # Reset index for easier viewing
    coding_df = coding_df.reset_index(drop=True)

    # Save to CSV for open coding
    output_path = save_dataframe(coding_df, 'open_coding_sample.csv', subfolder='processed')
    print(f"\nSaved {len(coding_df)} posts to {output_path}")
    print(f"\nColumns in coding file:")
    print(f"  - id: Post ID")
    print(f"  - title: Post title")
    print(f"  - opening_text: First ~500 chars of post text")
    print(f"  - text_for_coding: Combined title + opening (for easy reading)")
    print(f"  - subreddit: Source subreddit")
    print(f"  - topic: [EMPTY - Fill this in during open coding]")
    print(f"  - notes: [OPTIONAL - Add any notes here]")
    print(f"\nInstructions:")
    print(f"  1. Open {output_path} in Excel or a text editor")
    print(f"  2. Read the 'text_for_coding' column for each post")
    print(f"  3. Assign each post to exactly ONE topic in the 'topic' column")
    print(f"  4. Aim for 3-8 topics total")
    print(f"  5. Save your progress regularly")


if __name__ == "__main__":
    main()

