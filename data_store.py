favorites = []


def add_favorite(song):
    if song not in favorites:
        favorites.append(song)


def get_favorites():
    return favorites