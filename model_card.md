# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

VibeFinder 1.0

---

## 2. Intended Use

This system suggests songs from a small catalog based on a user's preferred genre,
mood, and numerical taste targets like energy and tempo. It is designed for classroom
exploration only, not for real users or production use. It assumes the user has a
single fixed taste profile and knows exactly what genre and mood they want.

---

## 3. How the Model Works

The system compares each song in the catalog to a user's taste profile and gives it
a score. A genre match adds the most points because genre is the strongest signal of
overall taste. A mood match adds slightly fewer points. For numerical features like
energy, tempo, valence, danceability, and acousticness, the system rewards songs that
are closest to the user's target value rather than just high or low. Once every song
has a score, the system sorts them from highest to lowest and returns the top results.
Think of it like a judge scoring contestants -- each song gets rated on how well it
matches what the user asked for, and the best matches rise to the top.

---

## 4. Data

The catalog contains 18 songs across genres including lofi, pop, rock, jazz, ambient,
synthwave, indie pop, r&b, country, classical, blues, and folk. Moods represented
include happy, chill, intense, relaxed, focused, moody, euphoric, and sad. The
original starter dataset had 10 songs, mostly lofi and pop. Eight songs were added to
improve genre and mood diversity. Pop and lofi still have more songs than other genres,
which affects recommendation quality for underrepresented tastes.

---

## 5. Strengths

The system works best for users who prefer lofi or pop because those genres have the
most songs in the catalog, giving the recommender more options to differentiate
between. The scoring logic is fully transparent -- every recommendation comes with a
breakdown of exactly why each song was chosen. The proximity formula for numerical
features is also a strength because it rewards close matches rather than just extreme
values, which makes recommendations feel more tuned to the user.

---

## 6. Limitations and Bias

The system has a strong genre bias because genre match is worth more than any single
numerical feature. A song that perfectly matches the user's energy, tempo, valence,
danceability, and acousticness can still lose to a mediocre song that shares the same
genre label. The catalog is unevenly distributed -- pop and lofi have multiple songs
each while rock, blues, and classical have only one, so users with those tastes get
weaker results after the first recommendation. This creates a filter bubble where users
are consistently shown the same small pool of songs. The system also treats all users
as having the same preference shape, assuming everyone wants an exact genre and mood
match with no room for discovery or mixed taste.

---

## 7. Evaluation

I tested the system with four profiles: Chill Lofi Studier, High Energy Pop Fan, Deep
Intense Rock, and Sad Acoustic. The lofi and pop profiles returned strong and varied
results. The rock and blues profiles showed a sharp drop in score after the first
result because only one song per genre exists in the catalog. I also ran a weight
experiment doubling the energy score and halving the genre score. Rankings shifted
slightly within profiles but genre remained the dominant signal even at half weight.
The biggest surprise was that Baby Steps ranked above Sunrise City for the pop profile
despite Sunrise City feeling like the more intuitive match, showing that technically
correct scores do not always produce musically satisfying results.

---

## 8. Future Work

- Add more songs per genre to reduce the drop-off problem for underrepresented tastes
- Implement a diversity penalty that prevents too many songs from the same genre
  appearing in the top results
- Add support for mixed taste profiles where a user can specify interest in multiple
  genres with different weights
- Replace exact genre matching with a similarity score so adjacent genres like
  synthwave and electronic can still earn partial points

---

## 9. Personal Reflection

Building this system made me realize how much of a recommendation is just math dressed
up to feel personal. The results feel like suggestions but they are really just
proximity scores on a spreadsheet. The most interesting discovery was how much genre
dominates the output even when I tried to reduce its weight -- which explains why real
platforms like Spotify can feel like they keep recommending the same type of music
over and over. It also made me think more critically about what is missing from simple
content-based systems: they have no memory, no sense of context, and no way to know
when a user wants something familiar versus something new.
