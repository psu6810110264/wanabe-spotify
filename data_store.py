import os

favorites = []

SONG_FILES = {
    "Midnight Dreams": "assets/music/midnight_dreams.mp3",
    "Summer Vibes": "assets/music/summer_vibes.mp3",
    "Electric Soul": "assets/music/electric_soul.mp3",
    "Ocean Radio": "assets/music/ocean_radio.mp3",
    "Moonlight Avenue": "assets/music/moonlight_avenue.mp3",
    "Deep Blue": "assets/music/deep_blue.mp3",
    "Pixel Heart": "assets/music/pixel_heart.mp3",
    "Red Skyline": "assets/music/red_skyline.mp3",
    "Chill Mix": "assets/music/chill_mix.mp3",
    "Night Drive": "assets/music/night_drive.mp3",
    "Acoustic Mood": "assets/music/acoustic_mood.mp3",
}


def add_favorite(song_title, artist_name="Unknown Artist", duration="0:00"):
    if not is_favorite(song_title, artist_name):
        favorites.append({
            "title": song_title,
            "artist": artist_name,
            "duration": duration,
        })
        return True
    return False


def remove_favorite(song_title, artist_name=None):
    for item in favorites[:]:
        if item["title"] == song_title and (artist_name is None or item["artist"] == artist_name):
            favorites.remove(item)
            return True
    return False


def is_favorite(song_title, artist_name=None):
    for item in favorites:
        if item["title"] == song_title and (artist_name is None or item["artist"] == artist_name):
            return True
    return False


def toggle_favorite(song_title, artist_name="Unknown Artist", duration="0:00"):
    if is_favorite(song_title, artist_name):
        remove_favorite(song_title, artist_name)
        return False
    add_favorite(song_title, artist_name, duration)
    return True


def get_favorites():
    return favorites


def clear_favorites():
    favorites.clear()


def get_song_file(song_title):
    path = SONG_FILES.get(song_title, "")
    if path and os.path.exists(path):
        return path
    return ""