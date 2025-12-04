# Project Requirements and Rubric Checklist

## Project Requirements Summary (Project 2: Movie Release)

### Required Components:

1. **Data Collection** ✓
   - ✅ Collect 500+ posts total on movies
   - ✅ Ensure all posts are in English
   - ✅ Collect articles without bias towards/against coverage volume
   - ✅ Set filters so all posts have high likelihood of being related to one of the movies

2. **Open Coding** ✓
   - ✅ Conduct open coding on 200 articles
   - ✅ Each article belongs to exactly one topic
   - ✅ Use title and opening of article (not entire article)
   - ✅ Aim for 3-8 topics total (You have 8 topics: 1a, 1b, 1c, 2, 3, 4, 5, 6)

3. **Manual Annotation** ✓
   - ✅ Manually annotate entire set of 500+ articles in dataset
   - ✅ Single annotation (not double annotation)

4. **Topic Characterization** ✓
   - ✅ Compute 10 words in each category with highest TF-IDF scores
   - ✅ Use LLM (ChatGPT) to produce representative summary of each category

5. **Research Questions** ✓
   - ✅ What aspect of the movie was the focus (topic) of the article?
   - ✅ How much coverage the movie received relative to other movies that came out at a similar time?

---

## Report Structure Requirements

### Required Sections (5-7 pages, not including references):

1. **Introduction (0.5 page)**
   - General overview
   - Key findings

2. **Data (0.5 page)**
   - Describe dataset
   - Statistics relevant to project
   - Number of articles collected
   - Filtering done
   - Design decisions around collection

3. **Methods (0.5 page)**
   - Explanation and justification for what you did
   - Focus on design decisions NOT listed in requirements document
   - Design decisions that impacted results

4. **Results (1 page)**
   - Share all findings including:
     - Topics selected (and their definitions)
     - Topic characterization
     - Topic engagement

5. **Discussion (1 page)**
   - Interpret results in terms of what they reveal
   - Make extensive use of results to justify interpretations

6. **Group Member Contributions (0.25 page)**
   - Description of contributions each group member made

7. **References (< 1 page)** (Optional)
   - Should you reference other works

### Formatting Requirements:
- ✅ Use AAAI Camera Ready format (LaTeX template provided)
- ✅ Follow template formatting strictly (font, font size, spacing, citation style)
- ✅ Figures encouraged but must be used to maximum effect
- ✅ Report must be 5-7 pages (not including references)

---

## Evaluation Rubric (100 points total)

### 1. Style (10 points)
- **+5 points**: Something you can understand with effort
- **+5 points**: Something you can easily understand
- **Check**: Clear, concise writing? Good grammar and spelling?

### 2. Data Collection Correctness (10 points)
- **+5 points**: Data that "works" but is hardly good
- **+5 points**: Data that works and EXPLICITLY addresses its limitations
- **Check**: 
  - Was dataset prepared correctly?
  - Was sampling done to avoid problematic biases?
  - Did it have baseline characteristics for meaningful insights?

### 3. Topic Design Validity (15 points) - Methods section
- **+7.5 points**: Reasonable indication that they did something reasonable
- **+7.5 points**: Clearly outline a method that will produce solid results (in line with class)
- **Check**: 
  - Was a process followed that would produce valid topics?
  - Insufficient details = not done

### 4. Topic Validity (15 points)
- **+5 points**: Definitions given
- **+5 points**: Suitability of the topics
- **+5 points**: Minimal subjectivity (very careful handling of "other" or out of bounds topic material)
- **Check**: 
  - Are topics appropriate to the task?
  - Are they well-defined?
  - Are they defined to minimize subjectivity?

### 5. Annotation Quality (10 points)
- **+5 points**: Some sort of annotation process that reflects the class
- **+5 points**: Sound process in line with the class
- **Check**: Does annotation process give confidence in quality of annotations?

### 6. Results (20 points)
- **10 points**: Topic distribution (across data)
- **10 points**: Topic characterization (TF-IDF)
- **Check**: 
  - Are all results requested present?
  - Do results make sense?
  - Are outliers or unusual trends appropriately explained?

### 7. Findings (20 points)
- **5 points**: Bigger picture point 1
- **5 points**: Bigger picture point 2
- **5 points**: Conclusion
- **5 points**: For "integration"
- **Check**: 
  - Are insightful interpretations provided?
  - Are these grounded in results?
  - Do findings integrate results and prior knowledge in a sound, well-reasoned way?

---

## Current Project Status Check

### ✅ Completed:
1. Data collection: 667 posts collected and annotated
2. Open coding: 8 topics created (1a, 1b, 1c, 2, 3, 4, 5, 6)
3. Manual annotation: All posts annotated with topics
4. TF-IDF analysis: Top 10 words computed for each topic
5. Topic summaries: Created (both manual and LLM-ready)
6. Research questions: Both questions addressed with analysis scripts

### 📝 To Do for Report:
1. **Write Introduction** (0.5 page)
   - General overview
   - Key findings summary

2. **Write Data Section** (0.5 page)
   - Dataset statistics (667 posts)
   - Collection period (July 1 - Aug 31, 2025)
   - Subreddits used (r/movies, r/boxoffice, r/DC_Cinematic, r/superman)
   - Filtering decisions (English only, movie-related)
   - Design decisions

3. **Write Methods Section** (0.5 page)
   - Open coding process (200 posts)
   - Topic design decisions (why 8 topics, why split Box Office by movie)
   - Annotation process
   - TF-IDF methodology
   - LLM summarization approach

4. **Write Results Section** (1 page)
   - Topic definitions (from codebook.md)
   - Topic distribution (from topic_distribution_summary.txt)
   - Topic characterization (TF-IDF top words from tfidf_top_words_by_topic.txt)
   - Topic summaries (from topic_summaries.txt)
   - Coverage comparison (from coverage_comparison_summary.txt)

5. **Write Discussion Section** (1 page)
   - Interpret findings for research question 1 (what aspects users focus on)
   - Interpret findings for research question 2 (relative coverage)
   - Ground interpretations in results
   - Connect to bigger picture

6. **Write Group Member Contributions** (0.25 page)

7. **Format in LaTeX** using AAAI template
   - Update title, author, abstract
   - Add all sections
   - Include figures if helpful
   - Ensure 5-7 pages

---

## LaTeX Template Notes

### Current Template Status:
- ✅ Template file: `LaTeX/anonymous-submission-latex-2024.tex`
- ✅ Uses `\usepackage[submission]{aaai24}` (correct for submission)
- ⚠️ Currently has example content - needs to be replaced with your content

### Key LaTeX Requirements:
- Title must be in Title Case (mixed case, not sentence case)
- Two-column format required
- Times Roman or Nimbus font (not Computer Modern)
- 10-point type with 12-point leading
- No page numbers, footers, or headers
- Figures must be .jpg, .png, or .pdf (not .gif, .ps, .eps)
- References must use natbib with aaai24.bst style

### For Final Submission:
- Remove `\usepackage[submission]{aaai24}` and use `\usepackage{aaai24}` (no submission option)
- Add author names and affiliations
- Add copyright notice (automatic with aaai24.sty)
- Clear PDF metadata

---

## Recommendations

1. **Start writing the report sections** using the data you've already generated
2. **Create visualizations** if helpful (topic distribution charts, coverage comparison charts)
3. **Review codebook.md** - it has excellent topic definitions you can use
4. **Use topic_summaries.txt** for the Results section
5. **Use RESEARCH_ANSWERS.md** as a starting point for Discussion section
6. **Ensure all 8 topics are well-defined** in the codebook (they are!)
7. **Document your annotation process** in Methods section
8. **Address limitations** of your data collection in Data section

