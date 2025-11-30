## Coding Codebook for Reddit Movie Posts

This codebook defines the main topic of each post. Assign one primary category to each post based on the text_for_coding field. Use "Other" or "General news" only when a post clearly does not fit the more specific categories.

### 1. Box Office and Financial Performance

Definition
- Posts primarily about money and performance metrics: grosses, admissions, drops, forecasts, presales, regional box office, or rankings where the focus is on financial outcomes.

Example
- id 1mp6ip9 – "Warner Bros. Superman has grossed an estimated $249.4M internationally... Estimated global total through Tuesday stands at $583.2M."

Negative example
- id 1lvlxbc – "James Gunn’s Superman is now Verified Hot with a 96% audience score on Rotten Tomatoes!" (this is audience reception, not revenue)

Edge case
- id 1m1lwcx – "Superman opened in France with 576k tickets sold... lagging behind Man of Steel’s 1M and Superman Returns’ 640k..." (there are comparisons, but they are comparisons of ticket counts, so still Box Office and Financial Performance)

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

### 3. Marketing, Release Strategy and Distribution

Definition
- Posts about how studios market and release films: marketing spend, trailers and TV spots, release timing, platform windows (theatrical vs PVOD/digital), and positioning decisions.

Example
- id 1m86yhj – "'Air Bud Returns': New Movie Sets Theatrical Release in Summer 2026" (news about a future theatrical release date, not about current performance)

Negative example
- id 1mgmnv1 – "Disney's The Fantastic Four: First Steps has grossed an estimated $43.9M from global IMAX screens..." (IMAX totals are still box office numbers, so Box Office and Financial Performance)

Edge case
- id 1lw88vs – international presale tracking for Superman and Fantastic Four with notes like "pre-sales range from meh to decent" and links to forecast articles. The main point is presale tracking and opening weekend expectations, so Box Office and Financial Performance. If a similar post focused mainly on when and where previews start or how a campaign is rolled out (rather than the numbers), it would move to Marketing, Release Strategy and Distribution.

---

### 4. IP, DCU and Franchise Strategy and Future Plans

Definition
- Posts about bigger-picture strategy around DCU/MCU or IP: slates, cancellations or greenlights, what current performance means for future titles, or general superhero/IP trends when framed as planning or strategy.

Example
- id 1m1aao0 – "If Fantastic Four underperforms/flops internationally like Superman, what does it mean for Supergirl or Clayface? Should Warner Bros worry about it?..." (uses current performance to reason about future DC titles and studio strategy)

Negative example
- id 1m5pls6 – detailed breakdown of Jurassic World Rebirth’s 3rd weekend numbers and projections (performance recap, not long term plans, so Box Office and Financial Performance)

Edge case
- id 1m7e018 – "‘Sinners’ and ‘Superman’ Are Hits, but Superheroes and Horror Movies Are No Longer Box Office Guarantees" (talks about superhero movies as a category and their reliability; focus is on state of the genre and implications, so IP, DCU and Franchise Strategy and Future Plans)

---

### 5. Film Quality, Creative Content and Characters

Definition
- Posts centered on what the movies are like as films: quality, tone, direction, scenes, character portrayals, comparisons of style or storytelling.

Example
- id 1mnbek2 – "I think James Gunn is much better at making DC films. The suicide squad is the GOTG formula perfected... Superman is Gunn at his most restrained - fantastic range." (evaluates Gunn’s films and stylistic range)

Negative example
- id 1mp6ip9 – Superman’s global totals (no comment on whether the movie is good or bad; purely financial, so Box Office and Financial Performance)

Edge case
- id 1mgevv4 – "I've just watched Man of Steel for the first time - after Gunn's Superman... I love the new movie... I have some thoughts..." (personal comparison of Man of Steel vs Gunn’s Superman focusing on experience and opinion, so Film Quality, Creative Content and Characters)

---

### 6. Fandom, Rankings and Community Meta Discussion

Definition
- Posts about fans, community behaviour, or how movies are discussed: rankings, personal viewing plans, worries about screenings, megathreads, or meta arguments about predictions and expectations.

Example
- id 1mtprjl – "Empty Theatre... I'm going to watch Fantastic Four tomorrow, and so far there has been only 1 seat booked except me... I'm worried if they will cancel the show..." (a fan discussing their own viewing experience and concerns)

Negative example
- id 1myy1kb – Jurassic World Rebirth’s weekend grosses and global total (standard performance update, so Box Office and Financial Performance)

Edge case
- id 1mp8eyr – "'Nobody 2' Review Thread... Rotten Tomatoes: Certified Fresh..." with a table of critic scores. This mixes community structure (review thread) with scores. If you focus on the thread as a community hub, use Fandom, Rankings and Community Meta Discussion. If you focus on the ratings, use Audience Reception and Scores. Be consistent within your annotation.

---

### 7. General News

Definition
- Posts that report general movie-related news that is not mainly about box office, audience scores, marketing strategy, franchise planning, film quality, or fandom behaviour.

Example
- id 1lrubj7 – "Julian McMahon Dies: ‘Nip/Tuck’, ‘Fantastic Four’, ‘FBI: Most Wanted’ Star Was 56" (reports an actor’s death without focusing on performance, reception, or strategy)

Negative example
- id 1m86yhj – "'Air Bud Returns': New Movie Sets Theatrical Release in Summer 2026" (this is mainly about a future release plan, so Marketing, Release Strategy and Distribution)

Edge case
- id 1mj4xdj – "Disney Boss Bob Iger Says ‘Creating New IP’ Is of ‘Great Value’ but There’s No ‘Priority’ Among Sequels, Remakes and Originals: Just ‘Great Movies’" (although it is a news headline, the content is about how a major studio thinks about IP and slates, so IP, DCU and Franchise Strategy and Future Plans)

### 8. Other

Definition
- Use this category only when a post does not reasonably fit any of the seven main categories above.

Examples
- Highly off-topic discussions with no meaningful connection to movies, box office, reception, strategy, quality, fandom, or news.

When in doubt between Box Office and Financial Performance and another category, default to Box Office and Financial Performance if the main content is numbers and money. Otherwise, pick the category that best matches the post’s central focus.

