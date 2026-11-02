import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    
    """
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        songs = []
        for row in reader:
            row["id"] = int(row["id"])
            for field in (
                "energy",
                "tempo_bpm",
                "valence",
                "danceability",
                "acousticness",
            ):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    
    """
    score = 0.0
    reasons = []

    def normalize_label(value: str) -> str:
        return "".join(character for character in value.casefold() if character.isalnum())

    if normalize_label(song["genre"]) == normalize_label(user_prefs["favorite_genre"]):
        score += 2.0
        reasons.append("Genre match (+2.0)")

    if normalize_label(song["mood"]) == normalize_label(user_prefs["favorite_mood"]):
        score += 1.0
        reasons.append("Mood match (+1.0)")

    energy_score = max(
        0.0,
        min(1.0, 1.0 - abs(user_prefs["target_energy"] - song["energy"])),
    )
    score += energy_score
    if energy_score > 0:
        reasons.append(f"Energy proximity (+{energy_score:.2f})")

    if user_prefs["likes_acoustic"] is True and song["acousticness"] > 0.5:
        score += 0.5
        reasons.append("Acoustic preference match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
   
    """
    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "; ".join(reasons) if reasons else "No preference matches."
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda recommendation: recommendation[1], reverse=True)
    return scored_songs[:max(0, k)]
