"""
Command line runner for the Music Recommender Simulation.
"""

import os
from src.recommender import load_songs, recommend_songs

user_prefs = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.38,
    "target_tempo_bpm": 75,
    "target_valence": 0.58,
    "target_danceability": 0.60,
    "target_acousticness": 0.80
}

high_energy_pop = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.90,
    "target_tempo_bpm": 128,
    "target_valence": 0.85,
    "target_danceability": 0.88,
    "target_acousticness": 0.08
}

deep_intense_rock = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.92,
    "target_tempo_bpm": 150,
    "target_valence": 0.45,
    "target_danceability": 0.65,
    "target_acousticness": 0.10
}

sad_acoustic = {
    "favorite_genre": "blues",
    "favorite_mood": "sad",
    "target_energy": 0.35,
    "target_tempo_bpm": 85,
    "target_valence": 0.33,
    "target_danceability": 0.50,
    "target_acousticness": 0.85
}

def main() -> None:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "songs.csv")
    songs = load_songs(csv_path)
    print(f"Loaded songs: {len(songs)}\n")

    profiles = {
        "Chill Lofi Studier": user_prefs,
        "High Energy Pop Fan": high_energy_pop,
        "Deep Intense Rock": deep_intense_rock,
        "Sad Acoustic": sad_acoustic
    }

    for profile_name, prefs in profiles.items():
        print(f"=== {profile_name} ===\n")
        recommendations = recommend_songs(prefs, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} by {song['artist']}")
            print(f"Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()

if __name__ == "__main__":
    main()