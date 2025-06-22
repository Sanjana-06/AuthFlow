# AuthFlow 🔐 | Django REST + Celery + Telegram Bot

AuthFlow is a secure backend application built with Django and Django REST Framework. It demonstrates integration with background task processing using Celery and Redis, and Telegram Bot support for user interaction.

## 📌 Features

- 🔐 Token-based Authentication (DRF)
- 📬 Celery background task to send welcome emails
- 🤖 Telegram Bot to collect usernames on `/start`
- 🧩 Redis as a message broker
- 🔐 Protected & Public API endpoints
- 🛠️ Clean, production-style code structure

---

## ⚙️ Tech Stack

- Python 3.12+
- Django 5.x
- Django REST Framework
- Celery 5.x
- Redis
- PostgreSQL / SQLite (your choice)
- Telegram Bot API
- httpx, dotenv

---
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Sanjana-06/AuthFlow.git
cd AuthFlow
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
```
### 5. Run Migrations
```bash
python manage.py migrate
```
### 6. Running the Project
```bash
python manage.py runserver
celery -A authFlowCore worker --loglevel=info
python telegramBot.py
```




