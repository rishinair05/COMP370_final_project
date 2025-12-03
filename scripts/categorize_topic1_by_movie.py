"""
Script to automatically categorize Topic 1 posts by movie.
Assigns subcategories: 1a=Superman, 1b=Jurassic World, 1c=Fantastic Four, 1d=Other/Smurfs

Run from project root: python scripts/categorize_topic1_by_movie.py
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
    text = str(row['selftext']).lower()[:500]  # First 500 chars for efficiency
    combined = title + ' ' + text
    
    # Check in order of specificity
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']):
        return '1a'  # Superman
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        return '1b'  # Jurassic World
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        return '1c'  # Fantastic Four
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        return '1d'  # Smurfs
    
    return '1d'  # Other


def categorize_topic1_by_movie():
    """Categorize Topic 1 posts by movie."""
    # Load Topic 1 data
    print("Loading topic1_for_subcategorization.csv...")
    data_path = get_data_path('processed') / 'topic1_for_subcategorization.csv'
    df = pd.read_csv(data_path)
    
    print(f"Total Topic 1 posts: {len(df)}")
    print()
    
    # Categorize by movie
    print("Categorizing posts by movie...")
    df['subcategory'] = df.apply(identify_movie, axis=1)
    
    # Count by subcategory
    print("\nCategorization results:")
    print("-" * 60)
    subcat_counts = df['subcategory'].value_counts().sort_index()
    subcat_names = {
        '1a': 'Superman',
        '1b': 'Jurassic World',
        '1c': 'Fantastic Four',
        '1d': 'Other/Smurfs'
    }
    
    for subcat in ['1a', '1b', '1c', '1d']:
        count = subcat_counts.get(subcat, 0)
        pct = (count / len(df) * 100) if len(df) > 0 else 0
        name = subcat_names.get(subcat, 'Unknown')
        print(f"  {subcat}. {name:20s}: {count:4d} posts ({pct:5.1f}%)")
    
    # Save updated CSV
    output_path = get_data_path('processed') / 'topic1_for_subcategorization.csv'
    df.to_csv(output_path, index=False)
    
    print(f"\n✓ Updated file saved to: {output_path}")
    print(f"\nThe 'subcategory' column now contains:")
    print("  - 1a: Superman Box Office")
    print("  - 1b: Jurassic World Box Office")
    print("  - 1c: Fantastic Four Box Office")
    print("  - 1d: Other/Smurfs Box Office")
    print()
    print("You can now use this file for your analysis!")


if __name__ == "__main__":
    categorize_topic1_by_movie()

