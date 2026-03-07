# Wanabe Spotify (grape music)

แอป Music Player ที่พัฒนาด้วย Python + Kivy/KivyMD โดยมีระบบล็อกอิน, เล่นเพลง, favorites และเพิ่มเพลงเองได้จากหน้า UI

## Features

- ระบบ `Login/Register` พร้อมบทบาทผู้ใช้ (`artist`, `listener`)
- หน้า `Home` แสดงเพลงตัวอย่างและเพลงที่ผู้ใช้เพิ่มเอง (`Your Added Songs`)
- หน้า `Player` เล่นเพลง, แสดง progress/time, seek, favorite, และ lyrics
- รองรับไฟล์เสียง `mp3`, `wav`, `ogg`, `mp4`
- เพิ่มเพลงใหม่ได้เฉพาะบัญชี `artist`
- หน้าเพิ่มเพลงมี:
	- อัปโหลดปกเพลง
	- อัปโหลดไฟล์เสียง
	- คำนวณ `Duration` อัตโนมัติจากไฟล์ (ไม่ต้องกรอกเอง)
	- ช่องกรอก `Lyrics` ตอนเพิ่มเพลง
- หน้า `Favorite` แสดงรายการเพลงที่กดหัวใจ

## Default Account

- Username: `admin`
- Password: `123456`
- Role: `artist`

## Tech Stack

- Python 3.11
- Kivy
- KivyMD
- pygame
- ffpyplayer

## Project Structure

```text
wanabe-spotify/
	main.py
	wanabe_spotify.kv
	data_store.py
	accounts.json
	requirements.txt
	assets/
		music/
	screen/
		add_song_screen.py
		favorite_screen.py
		home_screen.py
		login_screen.py
		player_screen.py
		profile_screen.py
		register_screen.py
		search_screen.py
	tests/
		test_data_store.py
		test_login.py
		test_player_stub.py
		test_song_flow.py
```

## Installation (Windows)

1. สร้าง virtual environment

```powershell
python -m venv .venv-1
```

2. เปิดใช้งาน venv

```powershell
.\.venv-1\Scripts\Activate.ps1
```

3. ติดตั้ง dependencies

```powershell
pip install -r requirements.txt
```

## Run Application

```powershell
python main.py
```

หรือถ้าต้องการระบุ interpreter ตรง ๆ:

```powershell
.\.venv-1\Scripts\python.exe .\main.py
```

## Run Tests

```powershell
.\.venv-1\Scripts\python.exe -m pytest -q
```

## How To Add Song

1. ล็อกอินด้วยบัญชีที่เป็น `artist`
2. เข้าหน้า `Add Song`
3. กรอก `Song Title`, `Artist`, `Category`, `Album`
4. กรอก `Lyrics` (ถ้าต้องการ)
5. อัปโหลด `Cover Image`
6. อัปโหลด `Audio File` เพื่อให้ระบบอ่าน `Duration` อัตโนมัติ
7. กด `Add Song`

หมายเหตุ:
- ถ้าไฟล์ `.mp4` เล่นไม่ได้ ให้ตรวจว่า install `ffpyplayer` แล้ว และ restart แอป

## Current Limitations

- ข้อมูลเพลงที่เพิ่มเองและ favorite เก็บในหน่วยความจำ (in-memory) ระหว่างรันโปรแกรม ยังไม่ persist ลงไฟล์
- ระบบค้นหาในหน้า Search ยังเป็น UI เป็นหลัก