# 🎵 MiniSpotify - Kivy Music Player

MiniSpotify เป็นแอปพลิเคชันเล่นเพลงขนาดเล็กที่พัฒนาด้วย Python และ Kivy  
โปรเจคนี้จำลองระบบพื้นฐานของ Spotify เช่น การเปิดเพลง การเปลี่ยนเพลง และระบบ Favorite

---

# 📦 Project Features

## 🔐 Login System
ผู้ใช้ต้องเข้าสู่ระบบก่อนใช้งาน

Username: admin  
Password: 123456

---

## 🏠 Home Screen
หน้าหลักของแอป

แสดงรายการเพลงยอดนิยม (Trending Now)

ผู้ใช้สามารถ
- เลือกเพลงเพื่อเปิดหน้า Player
- ดู Recommended Albums
- ใช้ Navigation bar เพื่อเปลี่ยนหน้า

---

## 🎧 Player Screen
หน้าจอเล่นเพลง

แสดงข้อมูล
- Song Title
- Artist Name

ปุ่มควบคุม

Prev → เล่นเพลงก่อนหน้า  
Play → เล่นเพลง  
Pause → หยุดเพลง  
Next → เพลงถัดไป  
Favorite → เพิ่มเพลงลงรายการโปรด  
Back to Home → กลับหน้า Home

---

## ⭐ Favorite System
ผู้ใช้สามารถกด Favorite จากหน้า Player

ระบบจะ
- บันทึกชื่อเพลงใน favorite list
- แสดงเพลงในหน้า Favorite
- ใช้ ScrollView สำหรับเลื่อนดูหลายเพลง

---

## 🔎 Search Screen
หน้าค้นหาเพลง

มี
- Search bar
- Popular searches

เวอร์ชันปัจจุบันเป็น UI สำหรับการค้นหา

---

## ❤️ Favorite Screen
แสดงเพลงที่ผู้ใช้กด Favorite

Features

- Dynamic favorite list
- Scrollable song list
- Navigation bar

---

# 🗂 Project Structure

wanabe-spotify/

main.py  
wanabe_spotify.kv  

data_store.py  

screen/

login_screen.py  
home_screen.py  
player_screen.py  
search_screen.py  
favorite_screen.py  

---

# ⚙️ Installation

ติดตั้ง Kivy

pip install kivy

---

# ▶ Run Application

python main.py

---

# 🚀 Development Progress

commit 21  
basic UI layout

commit 22  
login system

commit 23  
home screen and player screen

commit 24  
add favorite button

commit 25  
dynamic favorite list

---

# 📚 Technologies Used

Python  
Kivy  
ScreenManager  
KV Language

---

# 👨‍💻 Author

Student Project  
MiniSpotify Clone using Kivy