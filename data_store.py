import os
import json

favorites = []
current_user = ""
current_user_role = ""
custom_songs = []

ACCOUNTS_FILE = "accounts.json"
DEFAULT_ACCOUNTS = {
    "admin": {"password": "123456", "role": "artist"},
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

SONG_LYRICS = {
    "Midnight Dreams": "Under city lights we fade away\nChasing echoes of a better day\nHold on tight through the midnight sky",
    "Summer Vibes": "Warm wind, open road, no destination\nWe keep dancing with no hesitation\nSummer nights, we sing out loud",
    "Electric Soul": "Heartbeat syncing with the neon glow\nEvery step feels like a radio\nElectric soul, never letting go",
    "Ocean Radio": "Waves keep calling like a distant song\nOn this frequency we drift along\nOcean radio, play all night",
    "Moonlight Avenue": "Streetlights shining on the avenue\nEvery memory keeps leading back to you\nMoonlight paints the sky in blue",
    "Deep Blue": "Falling deeper where the silence flows\nIn the dark, a hidden fire glows\nDeep blue carries me back home",
    "Pixel Heart": "Pixel heart beating on the screen\nLove in colors never seen\nPress restart, we begin again",
    "Red Skyline": "Red skyline over sleepless streets\nEvery shadow moves with our heartbeat\nTill sunrise finds us young and free",
    "Chill Mix": "Slow down, breathe in, let the moment stay\nSoft drums washing all the noise away\nJust ride the night on a gentle wave",
    "Night Drive": "Windows down on an empty line\nCity sparks in the rearview shine\nNight drive, keep me in the light",
    "Acoustic Mood": "Two chords ringing in a quiet room\nSimple words begin to bloom\nAcoustic mood, tell the truth",
}


def _load_accounts():
    def default_accounts_copy():
        return {username: data.copy() for username, data in DEFAULT_ACCOUNTS.items()}

    def normalize_account(username, data):
        if isinstance(data, str):
            role = "artist" if username == "admin" else "listener"
            return {"password": data, "role": role}

        if isinstance(data, dict):
            password = data.get("password", "")
            role = str(data.get("role", "listener")).lower().strip()
            if role not in ("artist", "listener"):
                role = "listener"
            if isinstance(password, str) and password:
                return {"password": password, "role": role}

        return None

    if not os.path.exists(ACCOUNTS_FILE):
        return default_accounts_copy()

    try:
        with open(ACCOUNTS_FILE, "r", encoding="utf-8") as fp:
            data = json.load(fp)
        if isinstance(data, dict):
            accounts = default_accounts_copy()
            for username, account_data in data.items():
                if not isinstance(username, str):
                    continue
                normalized = normalize_account(username, account_data)
                if normalized:
                    accounts[username] = normalized
            return accounts
    except (OSError, json.JSONDecodeError):
        pass

    return default_accounts_copy()


def _save_accounts():
    with open(ACCOUNTS_FILE, "w", encoding="utf-8") as fp:
        json.dump(_accounts, fp, indent=2)


_accounts = _load_accounts()


def register_account(username, password, role="listener"):
    user = username.strip()
    role_value = role.strip().lower()

    if role_value not in ("artist", "listener"):
        return False, "Please select account type."

    if user in _accounts:
        return False, "Username already exists."

    _accounts[user] = {"password": password, "role": role_value}
    _save_accounts()
    return True, "Account created. Please login."


def authenticate_account(username, password):
    user = username.strip()
    account = _accounts.get(user)
    if not account:
        return False
    return account.get("password") == password


def get_account_role(username):
    user = username.strip()
    account = _accounts.get(user)
    if not account:
        return "listener"
    return account.get("role", "listener")


def set_current_user(username):
    global current_user, current_user_role
    current_user = username.strip()
    current_user_role = get_account_role(current_user)


def get_current_user():
    return current_user


def get_current_user_role():
    return current_user_role or "listener"


def clear_current_user():
    global current_user, current_user_role
    current_user = ""
    current_user_role = ""


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


def get_song_lyrics(song_title, artist_name=None):
    for song in custom_songs:
        if song["title"] == song_title and (artist_name is None or song["artist"] == artist_name):
            lyrics = song.get("lyrics", "").strip()
            if lyrics:
                return lyrics

    lyrics = SONG_LYRICS.get(song_title, "").strip()
    if lyrics:
        return lyrics

    return "No lyrics available for this song yet."


def add_custom_song(title, artist, duration, category="Other", album="Singles", cover_image_path="", audio_file_path=""):
    t = title.strip()
    a = artist.strip()
    d = duration.strip()
    c = category.strip() or "Other"
    al = album.strip() or "Singles"

    for song in custom_songs:
        if song["title"].lower() == t.lower() and song["artist"].lower() == a.lower():
            return False, "Song already exists in your list."

    custom_songs.append({
        "title": t,
        "artist": a,
        "duration": d,
        "category": c,
        "album": al,
        "cover_image_path": cover_image_path.strip(),
        "audio_file_path": audio_file_path.strip(),
    })
    return True, "Song added successfully."


def get_custom_songs():
    return custom_songs