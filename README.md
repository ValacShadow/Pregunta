# Pregunta – A Simple Q&A Website in Django

This is a Django-based web application inspired by Quora. It allows users to ask questions, answer others' questions, and like helpful answers.

---

## 🚀 Features

- ✅ User Registration
- ✅ User Login and Logout
- ✅ Ask Questions
- ✅ View All Questions
- ✅ View Answers to a Question
- ✅ Answer Any Question
- ✅ Like Any Answer
- ✅ Home Page showing Top 10 Questions by Answer Likes
- ✅ Answers sorted by most liked on question detail page
- ✅ Fully implemented using Django Forms
- ✅ Authentication-protected views


## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash

https://github.com/ValacShadow/Pregunta.git
git checkout dev
cd pregunta 

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```