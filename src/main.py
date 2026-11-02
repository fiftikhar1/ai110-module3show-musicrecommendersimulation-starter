"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

def main() -> None:
    songs = load_songs("data/songs.csv")
    profiles = {
        "High-Energy Pop": {
            "favorite_genre": "Pop",
            "favorite_mood": "Energetic",
            "target_energy": 0.9,
            "likes_acoustic": False,
        },
        "Chill Lofi": {
            "favorite_genre": "Lo-Fi",
            "favorite_mood": "Chill",
            "target_energy": 0.3,
            "likes_acoustic": True,
        },
        "Edge Case (Conflicting)": {
            "favorite_genre": "Rock",
            "favorite_mood": "Sad",
            "target_energy": 0.9,
            "likes_acoustic": True,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\nTop recommendations for {profile_name}:\n")
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
