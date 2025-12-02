# Analysis Summary: Answering Research Questions

This document summarizes the analysis performed to answer the two research questions.

## Research Questions

1. **What aspect of the movie was the focus (topic) of the article?**
   - Specifically: When Reddit users talk about Superman (2025), what aspects of the movie do they focus on?

2. **How much coverage the movie received relative to other movies that came out at a similar time?**
   - Specifically: How much relative Reddit coverage does Superman receive compared to the other major July 2025 releases - Jurassic World: Rebirth, Smurfs, and The Fantastic Four: First Steps?

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

**For Superman specifically:**
- **Box Office and Financial Performance**: 228 posts (58.5%) - Most discussed
- **Marketing, Franchise Strategy and Distribution**: 67 posts (17.2%) - Second most discussed
- **Fandom, Rankings and Community Meta Discussion**: 42 posts (10.8%) - Third most discussed
- **Film Quality, Creative Content and Characters**: 21 posts (5.4%)
- **Audience Reception and Scores**: 19 posts (4.9%)
- **General News**: 10 posts (2.6%)
- **Other**: 3 posts (0.8%)

**Overall pattern across all movies:**
- Box Office and Financial Performance dominates (71.4% of all posts)
- Marketing/Strategy is second (10.0%)
- Fandom discussions are third (6.7%)

### Question 2: Relative coverage comparison

**Total post counts:**
- **Superman**: 391 posts (41.2% of total) - Most covered
- **Fantastic Four**: 265 posts (27.9% of total)
- **Jurassic World**: 213 posts (22.4% of total)
- **Smurfs**: 38 posts (4.0% of total)

**Relative to Superman:**
- Fantastic Four: 67.8% of Superman's coverage
- Jurassic World: 54.5% of Superman's coverage
- Smurfs: 9.7% of Superman's coverage

**Coverage patterns:**
- Superman had the most consistent coverage over time
- Peak coverage for Superman: Weeks of July 7-13 and July 14-20 (73-74 posts each)
- Most coverage is in r/boxoffice subreddit (65.2% for Superman)
- Superman has unique coverage in r/DC_Cinematic (27.6% of Superman posts)

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

## How to Run the Analyses

```bash
# Answer Question 1: Topic distribution
python scripts/analyze_topic_distribution.py

# Answer Question 2: Coverage comparison
python scripts/analyze_coverage_comparison.py
```

## Next Steps

You can now:
1. Use the CSV files for further analysis or visualization
2. Create charts/graphs from the data
3. Write up your findings based on these results
4. Compare the topic distributions across different movies
5. Analyze temporal patterns in coverage

