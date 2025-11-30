# COMP 370 Final Project

## Project Structure

```
COMP370_final_project/
├── data/
│   ├── raw/              # Raw collected data
│   └── processed/        # Processed data for analysis
├── scripts/              # Executable scripts
│   ├── collect_reddit_posts.py
│   ├── prepare_open_coding.py
│   └── view_coding_progress.py
├── src/                  # Source code modules
│   ├── data_utils.py
│   └── text_processing.py
├── comp370/              # Python virtual environment
├── requirements.txt      # Python dependencies
└── README.md
```

## Question Formulation:

When Reddit users talk about Superman (2025), what aspects of the movie do they focus on?

How much relative Reddit coverage does Superman receive compared to the other major July 2025 releases - Jurassic World: Rebirth, Smurfs, and The Fantastic Four: First Steps.

## Data Collection:

Time Window: 2025-07-01 to 2025-08-31
Covers pre-release hype and over a month of reviews after.

Subreddits:
- r/movies and r/boxoffice for general movie discussion and performance discussions.
- Franchise Specific: r/DC_cinematic, r/superman for enthusiast reactions

Search Queries: new Superman movie, James Gunn Superman, Superman (2025)

Language: Restrict to only english posts. Use langdetect or langid and keep only rows where langdetect.detect(text) == 'en'

## Usage

### Setup
1. Activate virtual environment: `comp370\Scripts\activate` (Windows) or `source comp370/bin/activate` (Mac/Linux)
2. Install dependencies: `pip install -r requirements.txt`

### Running Scripts
All scripts should be run from the project root directory:

- **Collect Reddit posts**: `python scripts/collect_reddit_posts.py`
- **Prepare open coding sample**: `python scripts/prepare_open_coding.py`
- **View coding progress**: `python scripts/view_coding_progress.py`