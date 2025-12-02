"""
Script to analyze coverage comparison - Question 2:
How much coverage the movie received relative to other movies that came out at a similar time?

Compares the number of posts/articles for Superman vs other July 2025 releases.

Run from project root: python scripts/analyze_coverage_comparison.py
"""
import sys
from pathlib import Path
import pandas as pd
from datetime import datetime

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


def analyze_coverage_comparison():
    """Analyze coverage comparison across movies."""
    # Load annotated data
    print("Loading annotated_data.csv...")
    data_path = get_data_path('processed') / 'annotated_data.csv'
    df = pd.read_csv(data_path)
    
    print(f"Total posts in dataset: {len(df)}")
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
    
    # Convert timestamp to datetime
    df_expanded['date'] = pd.to_datetime(df_expanded['created_utc'], unit='s', errors='coerce')
    
    print("\n" + "=" * 80)
    print("COVERAGE COMPARISON ANALYSIS")
    print("=" * 80)
    
    # Count posts by movie
    print("\n1. TOTAL POST COUNT BY MOVIE")
    print("-" * 80)
    
    movie_counts = df_expanded['movie'].value_counts()
    total_posts = len(df_expanded)
    
    movies_of_interest = ['Superman', 'Jurassic World', 'Fantastic Four', 'Smurfs']
    
    for movie in movies_of_interest:
        count = movie_counts.get(movie, 0)
        pct = (count / total_posts * 100) if total_posts > 0 else 0
        print(f"  {movie:20s}: {count:4d} posts ({pct:5.1f}% of total)")
    
    other_count = movie_counts.get('Other', 0)
    print(f"  {'Other':20s}: {other_count:4d} posts")
    print(f"  {'TOTAL':20s}: {total_posts:4d} posts")
    
    # Coverage comparison (relative to Superman)
    print("\n\n2. RELATIVE COVERAGE (Compared to Superman)")
    print("-" * 80)
    
    superman_count = movie_counts.get('Superman', 0)
    
    if superman_count > 0:
        print(f"\nSuperman baseline: {superman_count} posts = 100%")
        print()
        
        for movie in ['Jurassic World', 'Fantastic Four', 'Smurfs']:
            count = movie_counts.get(movie, 0)
            ratio = (count / superman_count * 100) if superman_count > 0 else 0
            print(f"  {movie:20s}: {count:4d} posts ({ratio:5.1f}% of Superman's coverage)")
    
    # Coverage over time
    print("\n\n3. COVERAGE OVER TIME (By Week)")
    print("-" * 80)
    
    df_expanded['week'] = df_expanded['date'].dt.to_period('W')
    
    weekly_coverage = []
    for movie in movies_of_interest:
        movie_df = df_expanded[df_expanded['movie'] == movie]
        if len(movie_df) == 0:
            continue
        
        weekly = movie_df.groupby('week').size()
        for week, count in weekly.items():
            weekly_coverage.append({
                'movie': movie,
                'week': str(week),
                'count': count
            })
    
    weekly_df = pd.DataFrame(weekly_coverage)
    if len(weekly_df) > 0:
        print("\nWeekly post counts:")
        for movie in movies_of_interest:
            movie_weekly = weekly_df[weekly_df['movie'] == movie].sort_values('week')
            if len(movie_weekly) > 0:
                print(f"\n  {movie}:")
                for _, row in movie_weekly.iterrows():
                    print(f"    Week {row['week']}: {int(row['count'])} posts")
    
    # Coverage by subreddit
    print("\n\n4. COVERAGE BY SUBREDDIT")
    print("-" * 80)
    
    subreddit_coverage = []
    for movie in movies_of_interest:
        movie_df = df_expanded[df_expanded['movie'] == movie]
        if len(movie_df) == 0:
            continue
        
        subreddit_counts = movie_df['subreddit'].value_counts()
        print(f"\n  {movie}:")
        for subreddit, count in subreddit_counts.items():
            pct = (count / len(movie_df) * 100) if len(movie_df) > 0 else 0
            print(f"    r/{subreddit:15s}: {count:4d} posts ({pct:5.1f}%)")
            subreddit_coverage.append({
                'movie': movie,
                'subreddit': subreddit,
                'count': count,
                'percentage': pct
            })
    
    # Save results
    print("\n\n5. SAVING RESULTS")
    print("-" * 80)
    
    # Save movie counts
    counts_output = get_data_path('processed') / 'coverage_counts_by_movie.csv'
    counts_df = pd.DataFrame({
        'movie': movie_counts.index,
        'post_count': movie_counts.values,
        'percentage_of_total': [(c / total_posts * 100) for c in movie_counts.values]
    })
    counts_df = counts_df.sort_values('post_count', ascending=False)
    counts_df.to_csv(counts_output, index=False)
    print(f"Movie coverage counts saved to: {counts_output}")
    
    # Save relative coverage
    if superman_count > 0:
        relative_output = get_data_path('processed') / 'coverage_relative_to_superman.csv'
        relative_data = []
        for movie in movies_of_interest:
            count = movie_counts.get(movie, 0)
            ratio = (count / superman_count * 100) if superman_count > 0 else 0
            relative_data.append({
                'movie': movie,
                'post_count': count,
                'percentage_of_superman': ratio
            })
        relative_df = pd.DataFrame(relative_data)
        relative_df.to_csv(relative_output, index=False)
        print(f"Relative coverage saved to: {relative_output}")
    
    # Save weekly coverage
    if len(weekly_df) > 0:
        weekly_output = get_data_path('processed') / 'coverage_by_week.csv'
        weekly_df.to_csv(weekly_output, index=False)
        print(f"Weekly coverage saved to: {weekly_output}")
    
    # Save subreddit coverage
    if len(subreddit_coverage) > 0:
        subreddit_output = get_data_path('processed') / 'coverage_by_subreddit.csv'
        subreddit_df = pd.DataFrame(subreddit_coverage)
        subreddit_df.to_csv(subreddit_output, index=False)
        print(f"Subreddit coverage saved to: {subreddit_output}")
    
    # Save text summary
    summary_output = get_data_path('processed') / 'coverage_comparison_summary.txt'
    with open(summary_output, 'w', encoding='utf-8') as f:
        f.write("COVERAGE COMPARISON ANALYSIS - SUMMARY\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("RESEARCH QUESTION 2:\n")
        f.write("How much coverage the movie received relative to other movies?\n\n")
        
        f.write("TOTAL POST COUNT BY MOVIE:\n")
        f.write("-" * 80 + "\n")
        for movie in movies_of_interest:
            count = movie_counts.get(movie, 0)
            pct = (count / total_posts * 100) if total_posts > 0 else 0
            f.write(f"{movie:20s}: {count:4d} posts ({pct:5.1f}% of total)\n")
        
        f.write(f"\nTOTAL: {total_posts} posts\n")
        
        if superman_count > 0:
            f.write("\n\nRELATIVE COVERAGE (Compared to Superman):\n")
            f.write("-" * 80 + "\n")
            f.write(f"Superman baseline: {superman_count} posts = 100%\n\n")
            for movie in ['Jurassic World', 'Fantastic Four', 'Smurfs']:
                count = movie_counts.get(movie, 0)
                ratio = (count / superman_count * 100) if superman_count > 0 else 0
                f.write(f"{movie:20s}: {count:4d} posts ({ratio:5.1f}% of Superman's coverage)\n")
    
    print(f"Summary saved to: {summary_output}")
    print("\n" + "=" * 80)
    print("Analysis complete!")


if __name__ == "__main__":
    analyze_coverage_comparison()

