# Wanabe Spotify 🎧

Music Streaming Application built with Kivy.

## Team
- Member A
- Member B

## Project Overview
Wanabe Spotify is a Kivy-based music streaming application prototype inspired by a modern music player interface.  
The application was created as a group project to practice GUI development with Python and Kivy, including screen management, widget design, callback functions, and Git version control collaboration.

This project focuses on creating a clean and modern user interface with multiple screens such as Login, Home, Player, Search, and Favorite.  
It also demonstrates how different callbacks are used to control screen navigation and user interactions.

## Project Objectives
- To build a Kivy application with multiple screens
- To practice designing UI with many widgets
- To implement callback functions for navigation and interaction
- To use Git and GitHub for collaborative development
- To apply commit early and commit often during development

## Main Features
- Login screen with username and password validation
- Home screen with music list and recommended section
- Player screen with playback control buttons
- Search screen for browsing music
- Favorite screen for liked songs
- Screen navigation using ScreenManager
- Callback-based interaction between widgets and screens

## Application Screens

### 1. Login Screen
The Login Screen is the entry point of the application.  
Users must enter a valid username and password before accessing the main application.

**Functions used**
- `on_login()`
- `clear_fields()`

**Validation rules**
- Username and password cannot be empty
- Username must be at least 4 characters
- Password must be at least 6 characters
- Valid login:
  - Username: `admin`
  - Password: `123456`

---

### 2. Home Screen
The Home Screen displays the main music interface.  
It contains a trending music section, song cards, a search bar, and a recommended section.

**Functions used**
- `open_player(song_id)`
- `go_home()`
- `go_search()`
- `go_favorite()`
- `logout()`

**Main components**
- Music title section
- Search bar
- Trending song list
- Recommended albums
- Bottom navigation bar

---

### 3. Player Screen
The Player Screen shows the selected song and basic playback controls.

**Functions used**
- `back_home()`
- `on_play()`
- `on_pause()`
- `on_next()`
- `on_prev()`

**Main components**
- Song cover area
- Song title and artist name
- Playback controls
- Back to Home button

---

### 4. Search Screen
The Search Screen allows users to explore songs and switch to other screens using the bottom navigation.

**Functions used**
- `go_home()`
- `go_search()`
- `go_favorite()`

**Main components**
- Search input
- Popular search buttons
- Bottom navigation bar

---

### 5. Favorite Screen
The Favorite Screen contains a list of liked songs and allows users to open a selected song in the Player Screen.

**Functions used**
- `go_home()`
- `go_search()`
- `go_favorite()`
- `open_player(song_id)`

**Main components**
- Favorite song list
- Bottom navigation bar

## Widgets Used
This application uses more than 30 widgets in total.  
Examples of widgets used in the project include:

- `ScreenManager`
- `BoxLayout`
- `GridLayout`
- `ScrollView`
- `Label`
- `Button`
- `TextInput`
- `Widget`

## Callbacks Used
This project includes more than 10 callbacks.  
Examples of callbacks implemented:

1. `on_login()`
2. `clear_fields()`
3. `open_player(song_id)`
4. `go_home()`
5. `go_search()`
6. `go_favorite()`
7. `logout()`
8. `back_home()`
9. `on_play()`
10. `on_pause()`
11. `on_next()`
12. `on_prev()`

## Project Structure
```text
wanabe-spotify/
│
├── screen/
│   ├── __init__.py
│   ├── login_screen.py
│   ├── home_screen.py
│   ├── player_screen.py
│   ├── search_screen.py
│   └── favorite_screen.py
│
├── main.py
├── wanabe_spotify.kv
└── README.md