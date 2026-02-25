Хромов Александр Олегович

Студент группы - ИС-43

Сроки прохождения практики - 16.02.2026 по 01.03.2026

Тема практики - Администрирование информационных ресурсов

Вот нормальный README без воды, эмодзи, лицензий и лишнего.

---

API для управления учебным расписанием, группами, студентами, преподавателями и аудиториями.
Проект реализован на Python с использованием FastAPI и SQLite.

## Используемый стек
* Python 3.10+
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

## Архитектура

Проект реализует REST API для работы с базой данных учебного расписания.

База данных содержит следующие сущности:

* Groups — учебные группы
* Students — студенты
* Teachers — преподаватели
* Subjects — дисциплины
* Classrooms — аудитории
* Schedule — расписание занятий

Связи реализованы через внешние ключи.
Для расписания добавлена проверка конфликтов:

* Нельзя назначить преподавателя на две пары в одно время
* Нельзя использовать одну аудиторию в одно время
* Нельзя назначить группе две пары одновременно

## Структура проекта

```
chlmt_crm/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
└── crud.py
```

## Установка

Установить зависимости:

```
pip install fastapi uvicorn sqlalchemy pydantic
```

## Запуск проекта

```
uvicorn main:app --reload
```

После запуска API будет доступен по адресу:

```
http://127.0.0.1:8000
```

Интерактивная документация Swagger:

```
http://127.0.0.1:8000/docs
```

## Основные эндпоинты

### Groups

* POST /groups/
* GET /groups/
* DELETE /groups/{id}

### Students

* POST /students/
* GET /students/
* DELETE /students/{id}

### Teachers

* POST /teachers/
* GET /teachers/

### Subjects

* POST /subjects/
* GET /subjects/

### Classrooms

* POST /classrooms/
* GET /classrooms/

### Schedule

* POST /schedule/
* GET /schedule/

## Формат хранения расписания

В таблице schedule используются поля:

* group_id
* teacher_id
* subject_id
* classroom_id
* day_of_week (0–6)
* lesson_number (1–8)

Для группы установлено ограничение уникальности по:
(group_id, day_of_week, lesson_number)

## База данных

Используется SQLite.
Файл базы данных создаётся автоматически при первом запуске приложения:

```
chlmt.db
```

Дополнительная настройка сервера базы данных не требуется.

---

# Скриншот Сваггера

![[screenshot-swagger.png]]
