# Music Collection

Короткий веб-застосунок на Django для ведення власної колекції музичних альбомів, виконавців та треків з можливістю реєстрації та обмеженням прав редагування.

## Функціонал
- Перегляд списку альбомів, топ-альбомів та виконавців
- Реєстрація та авторизація користувачів
- Додавання, редагування та видалення власних альбомів (CRUD)
- Обмеження доступу до редагування чужих записів

## Технології
Python, Django, SQLite (розробка), Whitenoise, Gunicorn, django-environ

## Як запустити локально
```bash
git clone <посилання-на-ваш-репозиторій>
cd music_collection
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env       # та заповніть власний SECRET_KEY
python manage.py migrate
python manage.py runserver