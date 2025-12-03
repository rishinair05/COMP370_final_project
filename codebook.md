## Coding Codebook for Reddit Movie Posts

This codebook defines the main topic of each post. Assign one primary category to each post based on the text_for_coding field. Use "General news and Other" only when a post clearly does not fit the more specific categories.

### 1a. Box Office and Financial Performance - Superman

Definition
- Box office and financial performance posts specifically about Superman (2025), James Gunn's Superman, or DCU-related box office discussions. Includes grosses, admissions, drops, forecasts, presales, regional box office, or rankings where the focus is on financial outcomes related to Superman.

Example
- id 1mp6ip9 – "Warner Bros. Superman has grossed an estimated $249.4M internationally... Estimated global total through Tuesday stands at $583.2M."
- id 1lzzv2c – "July 11-13 Box Office Recap – 'Superman' flies to a great $125M debut domestically. However, it debuts with just $95M overseas, which is below expectations."

Negative example
- id 1lvlxbc – "James Gunn's Superman is now Verified Hot with a 96% audience score on Rotten Tomatoes!" (this is audience reception, not revenue)

Edge case
- id 1m1lwcx – "Superman opened in France with 576k tickets sold... lagging behind Man of Steel's 1M and Superman Returns' 640k..." (there are comparisons, but they are comparisons of ticket counts, so still Box Office and Financial Performance)

---

### 1b. Box Office and Financial Performance - Fantastic Four

Definition
- Box office and financial performance posts specifically about The Fantastic Four: First Steps. Includes grosses, admissions, drops, forecasts, presales, regional box office, or rankings where the focus is on financial outcomes related to Fantastic Four.

Example
- Posts about Fantastic Four's opening weekend, box office totals, financial performance metrics, or comparisons with other films' box office performance.

---

### 1c. Box Office and Financial Performance - Jurassic World and Other Movies

Definition
- Box office and financial performance posts about Jurassic World: Rebirth, Smurfs, or other movies not specifically categorized above. Also includes posts that discuss multiple movies' box office performance together without a clear focus on one specific film.

Example
- Posts about Jurassic World's box office performance, weekend grosses, international totals.
- Posts comparing multiple movies' box office performance.
- Posts about Smurfs or other movies' financial performance.

---

### 2. Audience Reception and Scores

Definition
- Posts focused on how audiences rate or react to movies: audience scores, CinemaScore, PostTrak, local rating platform scores, demographics and recommend rates.

Example
- id 1lply5b – "Jurassic World Rebirth Korean Audience Score... CGV score... Megabox score... Pros: ... universal praise for the CGI..." (discusses rating scores and qualitative audience praise)

Negative example
- id 1my366f – "Disney's The Fantastic Four: First Steps grossed an estimated $1.60M on Friday... Total domestic gross stands at $252.95M." (purely financial, so Box Office and Financial Performance)

Edge case
- id 1m9jaeu – "'The Fantastic Four: First Steps' gets an A- Cinemascore" (short but clearly about CinemaScore, so Audience Reception and Scores)

---

### 3. Marketing, Franchise Strategy and Distribution

Definition
- Posts about how studios position, market and plan their films and universes: marketing spend, trailers and TV spots, release timing, platform windows (theatrical vs PVOD/digital), slate priorities, cancellations or greenlights, and what current performance means for future titles.

Example
- id 1m86yhj – "'Air Bud Returns': New Movie Sets Theatrical Release in Summer 2026" (future theatrical release plan and positioning)

Negative example
- id 1my366f – "Disney's The Fantastic Four: First Steps grossed an estimated $1.60M on Friday... Total domestic gross stands at $252.95M." (purely financial performance, so Box Office and Financial Performance)

Edge cases
- id 1m1aao0 – "If Fantastic Four underperforms/flops internationally like Superman, what does it mean for Supergirl or Clayface? Should Warner Bros worry about it?..." (uses performance to reason about future DC titles and strategy, so Marketing, Franchise Strategy and Distribution)
- id 1m7e018 – "'Sinners' and 'Superman' Are Hits, but Superheroes and Horror Movies Are No Longer Box Office Guarantees" (discusses the state of superhero and horror movies as box office bets; focus is on genre and IP strategy, so also Marketing, Franchise Strategy and Distribution)

---

### 4. Film Quality, Creative Content and Characters

Definition
- Posts centered on what the movies are like as films: quality, tone, direction, scenes, character portrayals, comparisons of style or storytelling.

Example
- id 1mnbek2 – "I think James Gunn is much better at making DC films. The suicide squad is the GOTG formula perfected... Superman is Gunn at his most restrained - fantastic range." (evaluates Gunn's films and stylistic range)

Negative example
- id 1mp6ip9 – Superman's global totals (no comment on whether the movie is good or bad; purely financial, so Box Office and Financial Performance)

Edge case
- id 1mgevv4 – "I've just watched Man of Steel for the first time - after Gunn's Superman... I love the new movie... I have some thoughts..." (personal comparison of Man of Steel vs Gunn's Superman focusing on experience and opinion, so Film Quality, Creative Content and Characters)

---

### 5. Fandom, Rankings and Community Meta Discussion

Definition
- Posts about fans, community behaviour, or how movies are discussed: rankings, personal viewing plans, worries about screenings, megathreads, or meta arguments about predictions and expectations.

Example
- id 1mtprjl – "Empty Theatre... I'm going to watch Fantastic Four tomorrow, and so far there has been only 1 seat booked except me... I'm worried if they will cancel the show..." (a fan discussing their own viewing experience and concerns)

Negative example
- id 1myy1kb – Jurassic World Rebirth's weekend grosses and global total (standard performance update, so Box Office and Financial Performance)

Edge case
- id 1mp8eyr – "'Nobody 2' Review Thread... Rotten Tomatoes: Certified Fresh..." with a table of critic scores. This mixes community structure (review thread) with scores. If you focus on the thread as a community hub, use Fandom, Rankings and Community Meta Discussion. If you focus on the ratings, use Audience Reception and Scores. Be consistent within your annotation.

---

### 6. General News and Other

Definition
- Posts that report general movie-related news that is not mainly about box office, audience scores, marketing strategy, franchise planning, film quality, or fandom behaviour. Also includes highly off-topic discussions with no meaningful connection to movies, box office, reception, strategy, quality, or fandom.

Example
- id 1lrubj7 – "Julian McMahon Dies: 'Nip/Tuck', 'Fantastic Four', 'FBI: Most Wanted' Star Was 56" (reports an actor's death without focusing on performance, reception, or strategy)

Negative example
- id 1m86yhj – "'Air Bud Returns': New Movie Sets Theatrical Release in Summer 2026" (this is mainly about a future release plan, so Marketing, Franchise Strategy and Distribution)

Edge case
- id 1mj4xdj – "Disney Boss Bob Iger Says 'Creating New IP' Is of 'Great Value' but There's No 'Priority' Among Sequels, Remakes and Originals: Just 'Great Movies'" (although it is a news headline, the content is about how a major studio thinks about IP and slates, so Marketing, Franchise Strategy and Distribution)

When in doubt between Box Office and Financial Performance and another category, default to Box Office and Financial Performance if the main content is numbers and money. Otherwise, pick the category that best matches the post's central focus.
