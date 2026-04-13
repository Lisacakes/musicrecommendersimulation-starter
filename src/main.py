"""
Command line runner for the Music Recommender Simulation.
"""

import os
from src.recommender import load_songs, recommend_songs

def main() -> None:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "songs.csv")
    songs = load_songs(csv_path)

    user_prefs = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.38,
        "target_tempo_bpm": 75,
        "target_valence": 0.58,
        "target_danceability": 0.60,
        "target_acousticness": 0.80
    }

    print(f"Loaded songs: {len(songs)}")

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"{song['title']} by {song['artist']}")
        print(f"Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()

if __name__ == "__main__":
    main()