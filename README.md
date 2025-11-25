# COMP 370 Final Project

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