from data_store import favorites

def test_add_song():
    favorites.clear()

    song = "Song A"
    favorites.append(song)

    assert song in favorites

def test_favorites_not_empty():
    favorites.clear()

    favorites.append("Song B")

    assert len(favorites) > 0