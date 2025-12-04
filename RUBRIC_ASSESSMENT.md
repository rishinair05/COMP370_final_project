# Rubric Assessment: Project Evaluation Against Criteria

## 1. Data Collection Correctness (10 points)

### Questions:
- **Was the dataset prepared correctly?**
- **Was sampling done to avoid problematic biases?**
- **Did it have baseline characteristics that would allow this study to deliver meaningful insights?**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Data Collection Process:**
   - ✅ Collected 662 posts in final_dataset.xlsx (exceeds 500+ requirement)
   - ✅ Used multiple subreddits: r/movies, r/boxoffice, r/DC_Cinematic, r/superman
   - ✅ Time window: July 1 - Aug 31, 2025 (covers pre-release and post-release)
   - ✅ English filtering implemented using langdetect
   - ✅ Multiple search queries to capture different aspects
   - ✅ Deduplication by post ID
   - ✅ Dataset manually annotated and saved as final_dataset.xlsx

2. **Bias Mitigation:**
   - ✅ Multiple subreddits (not just fan communities)
   - ✅ Multiple search queries (not just "Superman")
   - ✅ Includes comparison movies (Fantastic Four, Jurassic World, Smurfs)
   - ✅ Time period covers full release cycle

#### ⚠️ POTENTIAL ISSUES TO ADDRESS:

1. **Subreddit Distribution Bias:**
   - Based on coverage analysis: r/boxoffice dominates (65-91% depending on movie)
   - r/DC_Cinematic: 28.4% of Superman posts (unique to Superman)
   - r/movies: 5-15% depending on movie
   - **Issue**: Heavy bias toward r/boxoffice may skew results toward box office discussions
   - **Recommendation**: Acknowledge this limitation in Data section. Explain that r/boxoffice naturally focuses on financial performance, which may explain why 65.8% of posts are box office-related.

2. **Search Query Bias:**
   - Queries include "new Superman movie", "James Gunn Superman", "Superman 2025" - all Superman-focused
   - Other movies have fewer/simpler queries
   - **Issue**: May have collected more Superman posts than other movies
   - **Recommendation**: Document this in Data section. Note that results show Superman received 41.3% of coverage, which may reflect both actual interest and collection method.

3. **Missing Documentation:**
   - No explicit discussion of sampling strategy
   - No discussion of potential biases
   - **Issue**: Rubric requires "EXPLICITLY address limitations"
   - **Recommendation**: Add a "Limitations" subsection in Data section discussing:
     - Subreddit distribution bias
     - Search query bias
     - Time period limitations
     - Language filtering effectiveness

### Score Estimate: **7-8/10**
- **+5 points**: Data works and is sufficient
- **+2-3 points**: Some acknowledgment of limitations, but needs to be more explicit
- **Missing**: Explicit discussion of biases and limitations

---

## 2. Topic Design Validity (15 points) - Methods Section

### Questions:
- **Was a process followed that would produce valid topics?**
- **Insufficient details should be treated the same as if something was not done.**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Open Coding Process:**
   - ✅ Script exists: `prepare_open_coding.py`
   - ✅ Sampled 200 posts randomly (random_state=42)
   - ✅ Used title + opening text (first 500 chars) as specified
   - ✅ Created codebook with definitions

2. **Topic Development:**
   - ✅ Started with open coding on 200 posts
   - ✅ Developed 8 topics (within 3-8 range)
   - ✅ Created detailed codebook with definitions, examples, negative examples, edge cases

#### ⚠️ GAPS TO ADDRESS:

1. **Missing Process Documentation:**
   - No written description of HOW open coding was conducted
   - No discussion of iterative refinement process
   - No explanation of how initial topics were refined into final 8 topics
   - **Issue**: Rubric says "Insufficient details = not done"
   - **Recommendation**: In Methods section, describe:
     - How open coding was performed (manual review, iterative categorization)
     - How initial categories were identified
     - How topics were refined (e.g., splitting Box Office by movie)
     - Rationale for final 8-topic structure

2. **Topic Refinement Process:**
   - Codebook shows sophisticated topic structure (1a, 1b, 1c for Box Office)
   - But no documentation of WHY this split was made
   - **Recommendation**: Explain in Methods:
     - Why Box Office was split by movie (to answer research question 2)
     - Why Topics 6 and 7 were merged
     - How the final structure addresses research questions

3. **Codebook Development:**
   - Codebook is excellent (definitions, examples, edge cases)
   - But no discussion of how it was developed
   - **Recommendation**: Describe codebook development process in Methods

### Score Estimate: **10-12/15**
- **+7.5 points**: Reasonable indication of process
- **+2.5-4.5 points**: Process exists but needs better documentation
- **Missing**: Detailed written description of the process

---

## 3. Topic Validity (15 points)

### Questions:
- **Are the topics appropriate to the task?**
- **Are they well-defined?**
- **Are they defined to minimize subjectivity?**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Topic Appropriateness:**
   - ✅ Topics directly address research questions
   - ✅ Box Office split by movie helps answer "relative coverage" question
   - ✅ Topics cover all major aspects: financial, reception, marketing, quality, fandom, news

2. **Topic Definitions:**
   - ✅ Excellent codebook with clear definitions
   - ✅ Each topic has:
     - Definition
     - Examples (with post IDs)
     - Negative examples (what NOT to include)
     - Edge cases (how to handle ambiguous cases)
   - ✅ "General News and Other" is clearly defined as catch-all

3. **Subjectivity Minimization:**
   - ✅ Clear decision rules (e.g., "when in doubt, default to Box Office if main content is numbers")
   - ✅ Edge cases documented
   - ✅ Negative examples help reduce ambiguity
   - ✅ Codebook provides guidance for borderline cases

#### ⚠️ MINOR ISSUES:

1. **Topic 5 (Fandom) vs Topic 2 (Audience Reception):**
   - Some overlap possible (e.g., review threads with scores)
   - Codebook acknowledges this with edge case guidance
   - **Status**: Well-handled with explicit guidance

2. **Topic 6 (General News) as Catch-All:**
   - Codebook says "use only when clearly doesn't fit"
   - This is appropriate and minimizes subjectivity
   - **Status**: Good

### Score Estimate: **13-15/15**
- **+5 points**: Excellent definitions
- **+5 points**: Topics are highly appropriate to task
- **+3-5 points**: Subjectivity well-minimized with clear rules

---

## 4. Annotation Quality (10 points)

### Questions:
- **Does the annotation process give us confidence in the quality of the annotations?**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Annotation Coverage:**
   - ✅ All 662 posts in final_dataset.xlsx have topics assigned (no missing annotations)
   - ✅ Used codebook for consistency
   - ✅ **Manual annotation confirmed**: Dataset was manually annotated (final_dataset.xlsx)

2. **Annotation Method:**
   - ✅ Codebook provides clear guidelines with definitions, examples, negative examples, and edge cases
   - ✅ Single annotation (as required)
   - ✅ 8-topic structure properly implemented (1a, 1b, 1c, 2, 3, 4, 5, 6)

#### ⚠️ ISSUES TO ADDRESS:

1. **Annotation Process Documentation:**
   - **Issue**: No written description of annotation workflow in Methods section
   - **Recommendation**: In Methods section, describe:
     - How manual annotations were performed (review of each post's title and opening text)
     - How codebook was used during annotation
     - Process for handling ambiguous cases
     - Any quality checks or review process performed

2. **Consistency Measures:**
   - Single annotation (as required), but no discussion of how consistency was maintained
   - **Recommendation**: Discuss in Methods:
     - How codebook was referenced during annotation
     - How edge cases were handled
     - Any self-review or consistency checks performed

### Score Estimate: **7-9/10**
- **+5 points**: Manual annotation was performed (confirmed)
- **+2-4 points**: Codebook exists and provides good guidance
- **Missing**: 
  - Written documentation of annotation process in Methods section
  - Discussion of consistency measures
  - Quality assurance documentation

### ✅ IMPROVED: Manual annotation confirmed. Main gap is documentation of the process in the Methods section.

---

## 5. Results (20 points)

### Questions:
- **Are all results requested present?**
- **Do the results make sense?**
- **Are outliers or unusual trends appropriately explained?**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Topic Distribution (10 points):**
   - ✅ Results present: `topic_distribution_summary.txt`
   - ✅ Overall distribution across all posts
   - ✅ Distribution for Superman specifically
   - ✅ Top 3 aspects identified
   - ✅ Results make sense (Box Office dominates, which aligns with r/boxoffice bias)

2. **Topic Characterization - TF-IDF (10 points):**
   - ✅ Top 10 words computed for each topic
   - ✅ Results in `tfidf_top_words_by_topic.txt`
   - ✅ TF-IDF scores provided
   - ✅ Words are appropriate (e.g., "superman", "weekend", "box office" for Topic 1a)
   - ✅ Topic summaries created

#### ⚠️ ISSUES TO ADDRESS:

1. **Outlier Explanations:**
   - **Outlier**: Box Office topics (1a+1b+1c) account for 65.8% of all posts (605/919 mentions)
   - **Explanation needed**: This should be explained (r/boxoffice bias: 65-91% of posts from r/boxoffice, natural focus on financial performance)
   - **Outlier**: Topic 2 (Audience Reception) only has 43 posts (4.7%)
   - **Explanation needed**: Why so few? Is this because scores are less discussed, or collection bias toward box office subreddit?

2. **Results Consistency:**
   - **Current dataset**: final_dataset.xlsx with 662 posts (all manually annotated)
   - **Topic distribution**: 919 total mentions (posts can mention multiple movies)
   - **Recommendation**: Clarify in Results section that:
     - 662 unique posts were analyzed
     - 919 total mentions because posts can discuss multiple movies
     - All analysis based on final_dataset.xlsx

3. **Missing Results:**
   - Topic summaries are present but not integrated into results
   - Coverage comparison results exist but may need better presentation

### Score Estimate: **17-19/20**
- **+9-10 points**: Topic distribution present, makes sense, and based on final_dataset.xlsx
- **+8-9 points**: TF-IDF characterization present, appropriate, and computed from final_dataset.xlsx
- **Minor gaps**: 
  - Explanation of outliers (Box Office dominance, low Audience Reception)
  - Clarification of 662 posts vs 919 mentions

---

## 6. Findings (20 points)

### Questions:
- **Are insightful interpretations provided?**
- **Are these grounded in results?**
- **Do the findings integrate results and prior knowledge in a sound, well-reasoned way?**

### Current Status Assessment:

#### ✅ STRENGTHS:
1. **Research Question 1 (What aspects?):**
   - ✅ Clear finding: Box Office topics combined dominate (65.8% of all mentions)
   - ✅ Grounded in results (topic distribution from final_dataset.xlsx)
   - ✅ Specific to Superman: 41.3% Box Office - Superman, 14.5% Marketing, 11.8% Fandom
   - ✅ Top 3 aspects clearly identified for Superman

2. **Research Question 2 (Relative coverage):**
   - ✅ Clear finding: Superman received most coverage (41.3% of total, 380 posts)
   - ✅ Grounded in results (coverage comparison from final_dataset.xlsx)
   - ✅ Relative percentages provided: Fantastic Four 67.1%, Jurassic World 53.9%, Smurfs 8.7%
   - ✅ Temporal patterns documented (weekly breakdown)
   - ✅ Subreddit distribution analyzed

#### ⚠️ GAPS TO ADDRESS:

1. **Interpretation Depth:**
   - Findings are descriptive but not deeply interpretive
   - **Missing**: 
     - What does "Box Office dominance" mean for how Reddit discusses movies?
     - Why might Superman get more coverage than other movies?
     - What does the topic distribution reveal about Reddit movie discourse?

2. **Integration with Prior Knowledge:**
   - No discussion of:
     - How Reddit movie discussions compare to other platforms
     - Whether box office focus is typical or unique
     - What prior research says about social media movie discourse
   - **Recommendation**: Add discussion connecting findings to broader context

3. **Bigger Picture Points:**
   - Rubric requires 2 "bigger picture" points
   - Current findings are more descriptive than interpretive
   - **Recommendation**: Develop 2 key insights:
     - E.g., "Reddit movie discourse is heavily financialized, focusing on box office performance over artistic merit"
     - E.g., "Superman's coverage dominance suggests higher community engagement, possibly due to DCU reboot interest"

4. **Conclusion:**
   - Basic conclusion present but could be stronger
   - **Recommendation**: Synthesize findings into a cohesive conclusion

### Score Estimate: **12-15/20**
- **+3-4 points**: Bigger picture point 1 (partially addressed)
- **+3-4 points**: Bigger picture point 2 (partially addressed)
- **+3-4 points**: Conclusion (basic)
- **+3 points**: Integration (needs work)
- **Missing**: 
  - Deeper interpretation
  - Integration with prior knowledge
  - Stronger bigger picture insights

---

## Summary of Critical Issues

### 🔴 CRITICAL (Must Fix):
1. **Methods Documentation**: Need detailed written description of:
   - Open coding process (how 200 posts were coded)
   - Topic development and refinement process
   - Annotation workflow (how manual annotation was performed)

2. **Data Limitations**: Must explicitly discuss biases in Data section:
   - Subreddit distribution bias (r/boxoffice dominates 65-91%)
   - Search query bias (Superman-focused queries)
   - Impact on results

### 🟡 IMPORTANT (Should Fix):
3. **Outlier Explanations**: Explain in Results/Discussion:
   - Why Box Office topics dominate (65.8% of mentions)
   - Why Audience Reception is small (4.7%)
   - Relationship between subreddit bias and topic distribution

4. **Findings Depth**: Develop deeper interpretations:
   - What Box Office dominance means for Reddit movie discourse
   - Why Superman gets more coverage
   - Integration with broader context/prior knowledge

5. **Clarify Dataset Numbers**: 
   - Explain 662 unique posts vs 919 total mentions (posts can mention multiple movies)
   - Ensure consistency throughout report

### 🟢 MINOR (Nice to Have):
6. **Topic Summaries**: Better integrate topic summaries into results section.

7. **Visualizations**: Consider adding figures to illustrate topic distribution and coverage comparison.

---

## Estimated Total Score: **70-82/100**

### Breakdown:
- Style: 8-10/10 (assuming good writing)
- Data Collection: 7-8/10 (needs explicit limitations discussion)
- Topic Design Validity: 10-12/15 (needs process documentation)
- Topic Validity: 13-15/15 ✅
- Annotation Quality: 7-9/10 ✅ (manual annotation confirmed, needs documentation)
- Results: 17-19/20 ✅ (based on final_dataset.xlsx)
- Findings: 12-15/20 (needs deeper interpretation)

### Priority Actions:
1. **Write detailed Methods section** describing:
   - Open coding process
   - Topic development process
   - Manual annotation workflow
2. **Add explicit limitations discussion** in Data section
3. **Develop deeper interpretations** in Discussion section
4. **Clarify dataset numbers** (662 posts vs 919 mentions)
5. **Explain outliers** (Box Office dominance, low Audience Reception)

