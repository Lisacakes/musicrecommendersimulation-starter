from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """Represents a song and its attributes."""
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
    """Represents a user's taste preferences."""
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """OOP implementation of the recommendation logic."""
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns a list of dictionaries."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, str]:
    """Scores a single song against user preferences and returns a score and explanation."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs.get("favorite_genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs.get("favorite_mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_score = 1 - abs(song["energy"] - user_prefs.get("target_energy", 0.5))
    score += energy_score
    reasons.append(f"energy closeness (+{energy_score:.2f})")

    tempo_score = 1 - abs(song["tempo_bpm"] - user_prefs.get("target_tempo_bpm", 100)) / 200
    score += tempo_score
    reasons.append(f"tempo closeness (+{tempo_score:.2f})")

    valence_score = 1 - abs(song["valence"] - user_prefs.get("target_valence", 0.5))
    score += valence_score
    reasons.append(f"valence closeness (+{valence_score:.2f})")

    danceability_score = 1 - abs(song["danceability"] - user_prefs.get("target_danceability", 0.5))
    score += danceability_score
    reasons.append(f"danceability closeness (+{danceability_score:.2f})")

    acousticness_score = 1 - abs(song["acousticness"] - user_prefs.get("target_acousticness", 0.5))
    score += acousticness_score
    reasons.append(f"acousticness closeness (+{acousticness_score:.2f})")

    explanation = ", ".join(reasons)
    return score, explanation

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs and returns the top k recommendations sorted by score."""
    scored = []
    for song in songs:
        score, explanation = score_song(user_prefs, song)
        scored.append((song, score, explanation))
    return sorted(scored, key=lambda x: x[1], reverse=True)[:k]