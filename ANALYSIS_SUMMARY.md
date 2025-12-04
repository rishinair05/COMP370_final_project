# Analysis Summary: Answering Research Questions

This document summarizes the analysis performed to answer the two research questions using the manually annotated dataset (`final_dataset.xlsx`).

## Research Questions

1. **What aspect of the movie was the focus (topic) of the article?**
   - Specifically: When Reddit users talk about Superman (2025), what aspects of the movie do they focus on?

2. **How much coverage the movie received relative to other movies that came out at a similar time?**
   - Specifically: How much relative Reddit coverage does Superman receive compared to the other major July 2025 releases - Jurassic World: Rebirth, Smurfs, and The Fantastic Four: First Steps?

## Dataset

- **Source**: `final_dataset.xlsx` (manually annotated)
- **Total posts**: 662 posts with topic annotations
- **Time period**: July 1 - August 31, 2025
- **Subreddits**: r/movies, r/boxoffice, r/DC_Cinematic, r/superman

## Analysis Scripts Created

### 1. `scripts/analyze_topic_distribution.py`
Answers Question 1 by analyzing:
- Overall topic distribution across all movies
- Topic distribution for each movie individually
- Detailed analysis for Superman posts
- Top 3 most discussed aspects of Superman

### 2. `scripts/analyze_coverage_comparison.py`
Answers Question 2 by analyzing:
- Total post counts for each movie
- Relative coverage compared to Superman
- Coverage over time (weekly breakdown)
- Coverage by subreddit

## Key Findings

### Question 1: What aspects do users focus on?

**For Superman specifically (380 posts):**
- **Box Office - Superman**: 157 posts (41.3%) - Most discussed
- **Marketing, Franchise Strategy and Distribution**: 55 posts (14.5%) - Second most discussed
- **Fandom, Rankings and Community Meta Discussion**: 45 posts (11.8%) - Third most discussed
- **Box Office - Fantastic Four**: 24 posts (6.3%) - Posts comparing Superman with Fantastic Four
- **Box Office - Jurassic World and Other Movies**: 25 posts (6.6%) - Posts comparing Superman with other movies
- **Film Quality, Creative Content and Characters**: 24 posts (6.3%)
- **General News and Other**: 29 posts (7.6%)
- **Audience Reception and Scores**: 19 posts (5.0%)

**Overall pattern across all movies (919 total post mentions):**
- **Box Office topics combined** (1a + 1b + 1c): 605 posts (65.8% of all posts)
  - Box Office - Superman: 274 posts (29.8%)
  - Box Office - Fantastic Four: 194 posts (21.1%)
  - Box Office - Jurassic World and Other: 137 posts (14.9%)
- **Marketing, Franchise Strategy and Distribution**: 69 posts (7.5%)
- **Fandom, Rankings and Community Meta Discussion**: 79 posts (8.6%)
- **General News and Other**: 73 posts (7.9%)
- **Film Quality, Creative Content and Characters**: 42 posts (4.6%)
- **Audience Reception and Scores**: 43 posts (4.7%)

### Question 2: Relative coverage comparison

**Total post counts (919 total mentions across all movies):**
- **Superman**: 380 posts (41.3% of total) - Most covered
- **Fantastic Four**: 255 posts (27.7% of total)
- **Jurassic World**: 205 posts (22.3% of total)
- **Smurfs**: 33 posts (3.6% of total)
- **Other**: 46 posts (5.0% of total)

**Relative to Superman:**
- Fantastic Four: 67.1% of Superman's coverage (255/380)
- Jurassic World: 53.9% of Superman's coverage (205/380)
- Smurfs: 8.7% of Superman's coverage (33/380)

**Coverage patterns:**
- **Superman** had the most consistent coverage over time, with peak coverage in weeks of July 7-13 (72 posts) and July 14-20 (74 posts)
- **Fantastic Four** had later peak coverage (week of July 21-27: 67 posts), suggesting delayed interest
- **Jurassic World** had early peak coverage (weeks of June 30-July 6 and July 7-13: 41-42 posts each)
- Most coverage is in r/boxoffice subreddit:
  - Superman: 65.8% in r/boxoffice, 28.4% in r/DC_Cinematic
  - Fantastic Four: 90.2% in r/boxoffice
  - Jurassic World: 91.2% in r/boxoffice
- Superman has unique coverage in r/DC_Cinematic (28.4% of Superman posts), reflecting franchise-specific interest

## Output Files Generated

### Question 1 Outputs:
- `data/processed/topic_distribution_overall.csv` - Overall topic counts and percentages
- `data/processed/topic_distribution_by_movie.csv` - Topic distribution broken down by movie
- `data/processed/topic_distribution_summary.txt` - Human-readable summary

### Question 2 Outputs:
- `data/processed/coverage_counts_by_movie.csv` - Total post counts per movie
- `data/processed/coverage_relative_to_superman.csv` - Relative coverage percentages
- `data/processed/coverage_by_week.csv` - Weekly coverage breakdown
- `data/processed/coverage_by_subreddit.csv` - Coverage by subreddit
- `data/processed/coverage_comparison_summary.txt` - Human-readable summary

### Topic Characterization:
- `data/processed/tfidf_top_words_by_topic.txt` - Top 10 TF-IDF words for each topic
- `data/processed/tfidf_top_words_by_topic.csv` - TF-IDF results in CSV format
- `data/processed/topic_summaries.txt` - Representative summaries of each topic category

## How to Run the Analyses

```bash
# Answer Question 1: Topic distribution
python scripts/analyze_topic_distribution.py

# Answer Question 2: Coverage comparison
python scripts/analyze_coverage_comparison.py

# Compute TF-IDF scores for topic characterization
python scripts/compute_tfidf_by_topic.py
```

## Next Steps

You can now:
1. Use the CSV files for further analysis or visualization
2. Create charts/graphs from the data
3. Write up your findings based on these results
4. Compare the topic distributions across different movies
5. Analyze temporal patterns in coverage
