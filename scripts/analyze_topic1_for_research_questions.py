import pandas as pd
import re
from datetime import datetime

df = pd.read_csv('data/processed/topic1_for_subcategorization.csv')

# Convert timestamp to datetime
df['date'] = pd.to_datetime(df['created_utc'], unit='s', errors='coerce')

# Identify movies mentioned
def identify_movie(row):
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:500]
    combined = title + ' ' + text
    
    movies = []
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu', 'dc cinematic']):
        movies.append('Superman')
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        movies.append('Jurassic World')
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        movies.append('Fantastic Four')
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        movies.append('Smurfs')
    
    return movies[0] if movies else 'Other'

df['movie'] = df.apply(identify_movie, axis=1)

# Categorize by type
def categorize_post(row):
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:1000]
    combined = title + ' ' + text
    
    # Expected
    if any(kw in combined for kw in ['forecast', 'predict', 'projection', 'tracking', 'presale', 
                                      'will it', 'could it', 'expected to', 'projected']):
        return 'Expected'
    
    # Actual Reports
    if any(kw in combined for kw in ['recap', 'weekend', 'friday', 'saturday', 'sunday', 
                                      'daily', 'total', 'cumulative', 'stands at']):
        return 'Actual Reports'
    
    # Analysis
    if any(kw in combined for kw in ['vs', 'versus', 'compared', 'comparison', 'behind', 
                                      'ahead', 'crossed', 'milestone', 'record', 'drop', 'decline']):
        return 'Analysis'
    
    return 'Other'

df['box_office_type'] = df.apply(categorize_post, axis=1)

# Determine if pre-release or post-release
# Assuming movies released around July 11-15, 2025
release_date = datetime(2025, 7, 11)
df['timing'] = df['date'].apply(lambda x: 'Pre-release' if pd.notna(x) and x < release_date else 'Post-release')

print("=" * 80)
print("TOPIC 1 SUBDIVISION OPTIONS FOR YOUR RESEARCH QUESTIONS")
print("=" * 80)
print()

print("RESEARCH QUESTION 1: What aspect of the movie was the focus?")
print("-" * 80)
print("Option A: Split by Box Office Type")
print(f"  1a. Expected/Predicted: {len(df[df['box_office_type'] == 'Expected'])} posts")
print(f"  1b. Actual Reports: {len(df[df['box_office_type'] == 'Actual Reports'])} posts")
print(f"  1c. Analysis/Comparisons: {len(df[df['box_office_type'] == 'Analysis'])} posts")
print("  → Helps understand: Are people discussing predictions or actual results?")
print()

print("Option B: Split by Movie Focus")
for movie in ['Superman', 'Jurassic World', 'Fantastic Four', 'Smurfs', 'Other']:
    count = len(df[df['movie'] == movie])
    if count > 0:
        print(f"  1a. {movie}: {count} posts")
print("  → Helps understand: Which movie gets more box office discussion?")
print()

print("Option C: Split by Timing (Pre vs Post Release)")
pre_count = len(df[df['timing'] == 'Pre-release'])
post_count = len(df[df['timing'] == 'Post-release'])
print(f"  1a. Pre-release Box Office: {pre_count} posts")
print(f"  1b. Post-release Box Office: {post_count} posts")
print("  → Helps understand: Are people discussing predictions or actual results?")
print()

print("RESEARCH QUESTION 2: How much coverage relative to other movies?")
print("-" * 80)
print("Option D: Split by Movie (MOST USEFUL FOR Q2)")
movie_counts = df['movie'].value_counts()
for movie, count in movie_counts.items():
    pct = (count / len(df) * 100)
    print(f"  {movie}: {count} posts ({pct:.1f}%)")
print("  → Directly answers: Which movie gets more box office coverage?")
print()

print("Option E: Split by Subreddit")
subreddit_counts = df['subreddit'].value_counts()
for subreddit, count in subreddit_counts.items():
    pct = (count / len(df) * 100)
    print(f"  r/{subreddit}: {count} posts ({pct:.1f}%)")
print("  → Helps understand: Where does box office discussion happen?")
print()

print("=" * 80)
print("RECOMMENDATIONS FOR YOUR RESEARCH QUESTIONS:")
print("=" * 80)
print()
print("For Question 1 (What aspect?):")
print("  → Use Option A (Expected/Actual Reports/Analysis)")
print("    This shows if people focus on predictions vs actual numbers vs analysis")
print()
print("For Question 2 (Relative coverage):")
print("  → Use Option D (Split by Movie)")
print("    This directly shows which movies get more box office discussion")
print()
print("COMBINED APPROACH (Best for both questions):")
print("  → Split Topic 1 by MOVIE (Superman, Jurassic World, Fantastic Four, Smurfs)")
print("    Then within each movie, you can see:")
print("    - How much box office coverage each movie gets (Q2)")
print("    - What type of box office discussion (expected vs actual) (Q1)")
print()

# Show breakdown by movie and type
print("=" * 80)
print("DETAILED BREAKDOWN: Movie × Box Office Type")
print("=" * 80)
for movie in ['Superman', 'Jurassic World', 'Fantastic Four', 'Smurfs']:
    movie_df = df[df['movie'] == movie]
    if len(movie_df) > 0:
        print(f"\n{movie} ({len(movie_df)} posts):")
        for botype in ['Expected', 'Actual Reports', 'Analysis', 'Other']:
            count = len(movie_df[movie_df['box_office_type'] == botype])
            if count > 0:
                pct = (count / len(movie_df) * 100)
                print(f"  {botype}: {count} ({pct:.1f}%)")

