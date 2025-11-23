 Overview
Mood Mirror is a lightweight emotional wellness web app that allows users to track daily moods, write reflections, review emotional history, and export entries. It focuses on clarity, ease of use, and calm design, making it ideal as a beginner full stack portfolio project.

Features
- Daily Mood Tracking: Choose how you feel each day.
- Optional Reflection Journaling:  Add short thoughts or notes.
- Mood History Page: View all previous entries in a clean list.
- Search Functionality: Find entries by mood or keyword.
- Export to JSON: Download your entire history anytime.
- Mobile-Responsive UI: Works smoothly on desktop and mobile.
- Soft Gradient UI Theme: Calming, minimalist wellness design.



 Tech Stack
Backend: Python/Flask
Frontend: HTML5, CSS3
Storage: JSON files (mood_data.json, exported data)
Additional Tools: VS Code, Git, GitHub

Project Structure

Mood Mirror/
─ app.py                 # Flask backend
─ static/
   ── style.css          # Styling & layout

── templates/
    ─ index.html         # Mood entry form
    ─ result.html        # Submission result page
    ─ history.html       # Mood history list
    ─ search.html        # Search tool
    ─ about.html         # About the app
---
── mood_data.json         # App generated mood storage
─ README.md              # Project documentation

How To Run This App
- You'd first need to clone this repository:
  git clone https://github.com/James120819/Mood-Mirror.git

- Navigate into the project folder:
  cd Mood-Mirror

- Install Flask:
  pip install flask

- Run the app:
  python app.py

- Open browser by clicking on:
  http://127.0.0.1:5000/



Feedback

Feedback and suggestions are appreciated! 
