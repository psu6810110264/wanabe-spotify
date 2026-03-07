import os
import json

favorites = []
current_user = ""
custom_songs = []

ACCOUNTS_FILE = "accounts.json"
DEFAULT_ACCOUNTS = {
    "admin": "123456",
}

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


def _load_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return DEFAULT_ACCOUNTS.copy()

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as fp:
            data = json.load(fp)
        if isinstance(data, dict):
            accounts = DEFAULT_ACCOUNTS.copy()
            for username, password in data.items():
                if isinstance(username, str) and isinstance(password, str):
                    accounts[username] = password
            return accounts
    except (OSError, json.JSONDecodeError):
        pass

    return DEFAULT_ACCOUNTS.copy()


def _save_accounts():
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as fp:
        json.dump(_accounts, fp, indent=2)


_accounts = _load_accounts()


def register_account(username, password):
    user = username.strip()
    if user in _accounts:
        return False, "Username already exists."

    _accounts[user] = password
    _save_accounts()
    return True, "Account created. Please login."


def authenticate_account(username, password):
    user = username.strip()
    return _accounts.get(user) == password


def set_current_user(username):
    global current_user
    current_user = username.strip()


def get_current_user():
    return current_user


def clear_current_user():
    global current_user
    current_user = ""


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


def get_song_file(song_title, artist_name=None):
    for song in custom_songs:
        if song["title"] == song_title and (artist_name is None or song["artist"] == artist_name):
            path = song.get("audio_file_path", "")
            if path and os.path.exists(path):
                return path

    path = SONG_FILES.get(song_title, "")
    if path and os.path.exists(path):
        return path
    return ""


def add_custom_song(title, artist, duration, cover_image_path="", audio_file_path=""):
    t = title.strip()
    a = artist.strip()
    d = duration.strip()

    for song in custom_songs:
        if song["title"].lower() == t.lower() and song["artist"].lower() == a.lower():
            return False, "Song already exists in your list."

    custom_songs.append({
        "title": t,
        "artist": a,
        "duration": d,
        "cover_image_path": cover_image_path.strip(),
        "audio_file_path": audio_file_path.strip(),
    })
    return True, "Song added successfully."


def get_custom_songs():
    return custom_songs