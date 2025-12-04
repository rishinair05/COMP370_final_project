# Research Questions Answers

Based on analysis of manually annotated dataset: `final_dataset.xlsx` (662 posts)

---

## Question 1: What aspect of the movie was the focus (topic) of the article?

### Summary
Based on the analysis of 662 manually annotated Reddit posts, the primary focus of discussions about movies is **Box Office and Financial Performance**, which accounts for 65.8% of all post mentions (605 out of 919 total mentions). This is followed by Fandom discussions (8.6%), General News (7.9%), Marketing/Strategy (7.5%), and other aspects.

**Note**: Posts can mention multiple movies, so total mentions (919) exceeds unique posts (662).

### Overall Topic Distribution (919 total mentions)

1. **Box Office and Financial Performance** (65.8% of all mentions)
   - 1a. Box Office - Superman: 274 mentions (29.8%)
   - 1b. Box Office - Fantastic Four: 194 mentions (21.1%)
   - 1c. Box Office - Jurassic World and Other: 137 mentions (14.9%)

2. **Fandom, Rankings and Community Meta Discussion**: 79 mentions (8.6%)

3. **General News and Other**: 73 mentions (7.9%)

4. **Marketing, Franchise Strategy and Distribution**: 69 mentions (7.5%)

5. **Film Quality, Creative Content and Characters**: 42 mentions (4.6%)

6. **Audience Reception and Scores**: 43 mentions (4.7%)

### Superman-Specific Topic Distribution (380 posts)

When Reddit users talk about Superman (2025), they focus on:

1. **Box Office - Superman**: 157 posts (41.3%) - Most discussed
   - Posts where Superman's box office performance is the main focus
   - Other movies can be mentioned for comparison, but Superman is primary

2. **Marketing, Franchise Strategy and Distribution**: 55 posts (14.5%) - Second most discussed
   - DCU strategy, James Gunn's plans, franchise direction

3. **Fandom, Rankings and Community Meta Discussion**: 45 posts (11.8%) - Third most discussed
   - Fan discussions, rankings, community engagement

4. **Box Office - Fantastic Four**: 24 posts (6.3%)
   - Posts comparing Superman with Fantastic Four box office

5. **Box Office - Jurassic World and Other Movies**: 25 posts (6.6%)
   - Posts comparing Superman with other movies' box office

6. **Film Quality, Creative Content and Characters**: 24 posts (6.3%)

7. **General News and Other**: 29 posts (7.6%)

8. **Audience Reception and Scores**: 19 posts (5.0%)

### Key Findings

- **Box Office dominates**: Over 65% of all mentions focus on financial performance, weekend grosses, and box office numbers
- **Superman gets most box office discussion**: 157 posts specifically about Superman's box office (41.3% of Superman posts)
- **Box Office split by movie helps answer research question 2**: The 1a/1b/1c structure allows tracking which movie is the main focus even when multiple movies are compared
- **Other aspects are less discussed**: Film quality (6.3%), audience reception (5.0%), and fandom (11.8%) each account for smaller portions of Superman discussions
- **Marketing/Strategy is second most discussed**: 14.5% of Superman posts focus on franchise strategy, reflecting interest in DCU direction

### Characteristic Words (TF-IDF)

- **Box Office - Superman (1a)**: "superman", "weekend", "week", "box office", "million", "estimated", "f1", "total"
- **Box Office - Fantastic Four (1b)**: "fantastic", "steps", "fantastic steps", "disney", "weekend", "box office", "total"
- **Box Office - Jurassic World (1c)**: "jurassic world", "jurassic", "rebirth", "world rebirth", "universal", "domestic"
- **Audience Reception (2)**: "audience", "cinemascore", "score", "gets cinemascore", "rotten tomatoes"
- **Marketing/Strategy (3)**: "gunn", "james gunn", "dcu", "superman", "new", "says", "dc"
- **Film Quality (4)**: "superman", "new", "movie", "new superman", "film", "scene", "like"
- **Fandom (5)**: "gunn", "james gunn", "superman", "fantastic", "dcu", "script"
- **General News (6)**: "jurassic", "jurassic world", "1m", "world", "rebirth", "day", "club"

---

## Question 2: How much coverage the movie received relative to other movies that came out at a similar time?

### Summary
**Superman (2025) received the most coverage** among the major July 2025 releases, with 380 post mentions (41.3% of total 919 mentions). Fantastic Four received 27.7% coverage (255 mentions), and Jurassic World received 22.3% coverage (205 mentions).

**Note**: Posts can mention multiple movies, so a single post can contribute to multiple movies' coverage counts. Total mentions (919) exceeds unique posts (662).

### Overall Coverage Comparison

| Movie | Total Mentions | Percentage of Total |
|-------|---------------|---------------------|
| **Superman** | 380 mentions | **41.3%** |
| Fantastic Four | 255 mentions | 27.7% |
| Jurassic World | 205 mentions | 22.3% |
| Smurfs | 33 mentions | 3.6% |
| Other | 46 mentions | 5.0% |
| **TOTAL** | **919 mentions** | **100%** |

### Relative Coverage (Compared to Superman)

Superman baseline: 380 mentions = 100%

- **Fantastic Four**: 255 mentions (67.1% of Superman's coverage)
- **Jurassic World**: 205 mentions (53.9% of Superman's coverage)
- **Smurfs**: 33 mentions (8.7% of Superman's coverage)

### Coverage Patterns

**Temporal Patterns:**
- **Superman**: Most consistent coverage over time
  - Peak weeks: July 7-13 (72 posts) and July 14-20 (74 posts)
  - Maintained strong coverage throughout the period
- **Fantastic Four**: Later peak coverage
  - Peak week: July 21-27 (67 posts)
  - Suggests delayed interest or later release timing
- **Jurassic World**: Early peak coverage
  - Peak weeks: June 30-July 6 (41 posts) and July 7-13 (42 posts)
  - Declined more rapidly over time

**Subreddit Distribution:**
- **r/boxoffice dominates** for all movies (65-91% of coverage)
  - Superman: 65.8% in r/boxoffice
  - Fantastic Four: 90.2% in r/boxoffice
  - Jurassic World: 91.2% in r/boxoffice
- **Superman has unique coverage** in r/DC_Cinematic (28.4% of Superman posts)
  - This reflects franchise-specific fan interest
  - Other movies lack this dedicated fan subreddit presence

### Box Office Coverage (Most Discussed Aspect)

Since Box Office is the dominant topic (65.8% of all mentions), the box office coverage directly shows relative interest:

| Movie | Box Office Mentions | Percentage of Box Office Mentions |
|-------|---------------------|-----------------------------------|
| **Superman** | 274 mentions | **45.3%** |
| Fantastic Four | 194 mentions | 32.1% |
| Jurassic World | 137 mentions | 22.6% |

### Key Findings

- **Superman dominates overall coverage**: Receives 41.3% of all mentions, more than any other movie
- **Fantastic Four is second**: 27.7% of total coverage, 67.1% of Superman's coverage
- **Jurassic World is third**: 22.3% of total coverage, 53.9% of Superman's coverage
- **Superman leads in box office discussions**: 45.3% of all box office mentions focus on Superman
- **Superman has broader topic diversity**: While all movies are discussed primarily in r/boxoffice, Superman has significant presence in r/DC_Cinematic (28.4%), suggesting stronger franchise-specific engagement
- **Coverage timing differs**: Superman had early and sustained coverage; Fantastic Four peaked later; Jurassic World peaked early but declined

### Conclusion

Superman (2025) received significantly more Reddit coverage than the other major July 2025 releases, with 41.3% of all mentions. This dominance is particularly evident in box office discussions, where Superman accounts for 45.3% of all box office mentions. The coverage patterns suggest:

1. **Higher community interest**: Superman's consistent coverage and presence in franchise-specific subreddits indicates stronger community engagement
2. **DCU reboot interest**: The high percentage of Marketing/Strategy discussions (14.5% of Superman posts) reflects interest in the DCU direction under James Gunn
3. **Box office focus**: The dominance of box office topics (65.8% overall) reflects Reddit's focus on financial performance, particularly in r/boxoffice subreddit

The relative coverage (Fantastic Four at 67.1%, Jurassic World at 53.9% of Superman's coverage) suggests that while Superman received the most attention, the other major releases also generated substantial discussion, with Fantastic Four receiving nearly two-thirds of Superman's coverage level.
