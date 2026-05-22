# Smarty Class Track 🎓

> "The class of yours deserve better, be smart and tracky"

**Live App:** https://web-production-add06e.up.railway.app/

## Demo Video
[![Smarty Class Track - How to Use](https://img.youtube.com/vi/9DVuNIcMTrU/0.jpg)](https://www.youtube.com/watch?v=9DVuNIcMTrU)

---

## What is this?

A Flask-based classroom management web app built for teachers. Frontend + Backend, fully deployed. Built this as a personal project to learn Python + Flask.

**Some things to note:** I used AI for CSS features like shadow and font as I was an intermediate beginner. In Python, when indentation and minimal things were affecting output and I felt helpless, I used it to debug. This is the first version so there will be bugs.

---

## Features

- 👨‍🎓 **Student Management** — add and manage your class roster
- 📋 **Mark Attendance** — mark present/absent daily with date tracking
- 📅 **View Attendance** — check past records
- ✏️ **Test Scores** — enter theory + practical marks, auto grade calculation
- 📊 **View Scores** — grouped by subject with class average
- 📄 **Report Cards** — full report per student
- 🧠 **Quiz Generator** — create MCQ quizzes, take them, see your score

---

## Tech Stack

- Python + Flask
- HTML / CSS / JS
- Deployed on Railway via GitHub

---

## Project Structure
Smarty-class-track/
├── app.py
├── students.txt
├── attendance.txt
├── scores.txt
├── quiz.txt
├── templates/
│   ├── index.html
│   ├── students.html
│   ├── attendance.html
│   ├── view_attendance.html
│   ├── scores.html
│   ├── view_scores.html
│   ├── report_card.html
│   ├── report.html
│   ├── quiz.html
│   ├── add_question.html
│   └── quiz_result.html
└── static/
├── style.css
├── scores.css
└── images/
## How to Run Locally

```bash
pip install flask
python app.py
```

Then open `http://127.0.0.1:5000`

---

## Goals for Next Version

- Improve UI
- Add calculator
- Add Jinja templated bot
- See more on code TODOs

---

## Dedicated to

The Horizons Team who will review it, and my school staff who got me into coding.

*— Made by Atharva*
