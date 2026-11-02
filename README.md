# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
Song Features: Tracks data including genre, mood, energy, tempo_bpm, valence, danceability, and acousticness.
UserProfile Data: Stores user preferences: favorite_genre, favorite_mood, target_energy, and a boolean likes_acoustic.
Genre and mood awards full points for exact text matches with favorite_genre and favorite_mood, energy and acousticness calculates proximity scores based on how close energy is to target_energy (
1−∣target−actual∣) and whether acousticness matches likes_acoustic. The scores are weighted and summed into a single compatibility score per song. For choosing recommendations, the Recommender scores every song in the dataset, ranks them from highest score to lowest, and returns the top 
k matches.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
Top recommendations:

Library Rain - Score: 4.45
Because: Genre match (+2.0); Mood match (+1.0); Energy proximity (+0.95); Acoustic preference match (+0.5)

Midnight Coding - Score: 4.38
Because: Genre match (+2.0); Mood match (+1.0); Energy proximity (+0.88); Acoustic preference match (+0.5)

Focus Flow - Score: 3.40
Because: Genre match (+2.0); Energy proximity (+0.90); Acoustic preference match (+0.5)

Spacewalk Thoughts - Score: 2.48
Because: Mood match (+1.0); Energy proximity (+0.98); Acoustic preference match (+0.5)

Winter Glass - Score: 1.44
Because: Energy proximity (+0.94); Acoustic preference match (+0.5)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---
when I added 3 total users
Top recommendations for High-Energy Pop:                           

Gym Hero - Score: 2.97
Because: Genre match (+2.0); Energy proximity (+0.97)

Sunrise City - Score: 2.92
Because: Genre match (+2.0); Energy proximity (+0.92)

Storm Runner - Score: 0.99
Because: Energy proximity (+0.99)

Neon Palms - Score: 0.96
Because: Energy proximity (+0.96)

Corner Store Freestyle - Score: 0.88
Because: Energy proximity (+0.88)


Top recommendations for Chill Lofi:

Library Rain - Score: 4.45
Because: Genre match (+2.0); Mood match (+1.0); Energy proximity (+0.95); Acoustic preference match (+0.5)

Midnight Coding - Score: 4.38
Because: Genre match (+2.0); Mood match (+1.0); Energy proximity (+0.88); Acoustic preference match (+0.5)

Focus Flow - Score: 3.40
Because: Genre match (+2.0); Energy proximity (+0.90); Acoustic preference match (+0.5)

Spacewalk Thoughts - Score: 2.48
Because: Mood match (+1.0); Energy proximity (+0.98); Acoustic preference match (+0.5)

Winter Glass - Score: 1.44
Because: Energy proximity (+0.94); Acoustic preference match (+0.5)


Top recommendations for Edge Case (Conflicting):

Storm Runner - Score: 2.99
Because: Genre match (+2.0); Energy proximity (+0.99)

Little Victories - Score: 1.21
Because: Energy proximity (+0.71); Acoustic preference match (+0.5)

Marigold Steps - Score: 1.04
Because: Energy proximity (+0.54); Acoustic preference match (+0.5)

Midnight Coding - Score: 1.02
Because: Energy proximity (+0.52); Acoustic preference match (+0.5)

Focus Flow - Score: 1.00
Because: Energy proximity (+0.50); Acoustic preference match (+0.5)
## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

this was my output:

Top recommendations for High-Energy Pop:                           

Gym Hero - Score: 2.94
Because: Genre match (+1.0); Energy proximity (+1.94)

Sunrise City - Score: 2.84
Because: Genre match (+1.0); Energy proximity (+1.84)

Storm Runner - Score: 1.98
Because: Energy proximity (+1.98)

Neon Palms - Score: 1.92
Because: Energy proximity (+1.92)

Corner Store Freestyle - Score: 1.76
Because: Energy proximity (+1.76)


Top recommendations for Chill Lofi:

Library Rain - Score: 4.40
Because: Genre match (+1.0); Mood match (+1.0); Energy proximity (+1.90); Acoustic preference match (+0.5)

Midnight Coding - Score: 4.26
Because: Genre match (+1.0); Mood match (+1.0); Energy proximity (+1.76); Acoustic preference match (+0.5)

Spacewalk Thoughts - Score: 3.46
Because: Mood match (+1.0); Energy proximity (+1.96); Acoustic preference match (+0.5)

Focus Flow - Score: 3.30
Because: Genre match (+1.0); Energy proximity (+1.80); Acoustic preference match (+0.5)

Winter Glass - Score: 2.38
Because: Energy proximity (+1.88); Acoustic preference match (+0.5)


Top recommendations for Edge Case (Conflicting):

Storm Runner - Score: 2.98
Because: Genre match (+1.0); Energy proximity (+1.98)

Gym Hero - Score: 1.94
Because: Energy proximity (+1.94)

Neon Palms - Score: 1.92
Because: Energy proximity (+1.92)

Little Victories - Score: 1.92
Because: Energy proximity (+1.42); Acoustic preference match (+0.5)

Sunrise City - Score: 1.84
Because: Energy proximity (+1.84)

pretty similar, but the chill lofi surprised me the most.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



