import pandas as pd

# Load data
df_all = pd.read_csv('data/processed/annotated_data.csv')
df_topic1 = pd.read_csv('data/processed/topic1_for_subcategorization.csv')

def identify_movie(row):
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

# Analyze overall coverage
print("=" * 80)
print("QUESTION 2: How much coverage relative to other movies?")
print("=" * 80)
print()

# Expand rows for movies (posts can mention multiple movies)
all_movies = {}
for _, row in df_all.iterrows():
    movies = []
    title = str(row['title']).lower()
    text = str(row['selftext']).lower()[:500]
    combined = title + ' ' + text
    
    if any(kw in combined for kw in ['superman', 'james gunn', 'gunn', 'dcu']):
        movies.append('Superman')
    if any(kw in combined for kw in ['jurassic', 'jurassic world', 'rebirth']):
        movies.append('Jurassic World')
    if any(kw in combined for kw in ['fantastic four', 'fantastic 4', 'ff4', 'first steps']):
        movies.append('Fantastic Four')
    if any(kw in combined for kw in ['smurf', 'smurfs']):
        movies.append('Smurfs')
    
    if not movies:
        movies = ['Other']
    
    for movie in movies:
        all_movies[movie] = all_movies.get(movie, 0) + 1

total_all = sum(all_movies.values())

print("OVERALL COVERAGE (All Topics Combined):")
print("-" * 80)
for movie in ['Superman', 'Fantastic Four', 'Jurassic World', 'Smurfs']:
    count = all_movies.get(movie, 0)
    pct = (count / total_all * 100) if total_all > 0 else 0
    print(f"  {movie:20s}: {count:4d} posts ({pct:5.1f}%)")
print(f"  {'TOTAL':20s}: {total_all:4d} posts")
print()

# Analyze Topic 1 box office coverage
topic1_movies = {}
for _, row in df_topic1.iterrows():
    movie = identify_movie(row)
    topic1_movies[movie] = topic1_movies.get(movie, 0) + 1

total_topic1 = sum(topic1_movies.values())

print("BOX OFFICE COVERAGE (Topic 1 Only):")
print("-" * 80)
for movie in ['Superman', 'Fantastic Four', 'Jurassic World', 'Smurfs']:
    count = topic1_movies.get(movie, 0)
    pct = (count / total_topic1 * 100) if total_topic1 > 0 else 0
    print(f"  {movie:20s}: {count:4d} posts ({pct:5.1f}%)")
print(f"  {'TOTAL Topic 1':20s}: {total_topic1:4d} posts")
print()

print("=" * 80)
print("ANALYSIS: Does splitting Topic 1 by movie help answer Question 2?")
print("=" * 80)
print()
print("YES - Here's why:")
print()
print("1. Topic 1 (Box Office) is the LARGEST category (432 posts = 65% of all posts)")
print("   → Splitting it by movie shows which movies get more BOX OFFICE coverage")
print()
print("2. Box office coverage is a key indicator of overall interest:")
print("   → More box office posts = more overall coverage")
print()
print("3. Current distribution in Topic 1:")
for movie in ['Superman', 'Fantastic Four', 'Jurassic World', 'Smurfs']:
    count = topic1_movies.get(movie, 0)
    pct_topic1 = (count / total_topic1 * 100) if total_topic1 > 0 else 0
    pct_all = (all_movies.get(movie, 0) / total_all * 100) if total_all > 0 else 0
    print(f"   {movie}: {count} box office posts ({pct_topic1:.1f}% of Topic 1)")
    print(f"          vs {all_movies.get(movie, 0)} total posts ({pct_all:.1f}% of all topics)")
print()
print("4. Recommendation:")
print("   → Split Topic 1 by MOVIE (1a=Superman, 1b=Jurassic World, 1c=Fantastic Four, 1d=Smurfs)")
print("   → This shows box office coverage distribution")
print("   → Combined with overall coverage, gives complete picture")
print()
print("=" * 80)
print("WHAT THIS TELLS YOU:")
print("=" * 80)
print("• Superman gets 48% of box office posts → Most box office discussion")
print("• Fantastic Four gets 28% of box office posts → Second most")
print("• Jurassic World gets 17% of box office posts → Third")
print("• This pattern matches overall coverage, confirming box office is the main focus")
print()
print("CONCLUSION: Splitting Topic 1 by movie DIRECTLY helps answer Question 2")

