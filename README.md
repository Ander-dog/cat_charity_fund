# Краткое описание

Сервис собирает пожертвования на различные целевые проекты: лечение, еду, кров и другую помощь хвостатым друзьям

# Порядок запуска приложения 

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать базу данных и применить миграции:

```
alembic upgrade head
```


# Список использованных технологий

- Python (язык разработки)
- FastAPI (фрэймворк приложения)
- Uvicorn (ASGI-сервер)
- SQLAlchemy (для работы с базами данных)
- Alembic (для создания миграций)
- Pydantic (для создания схем)

# Автор

[Андрей А.](https://github.com/Ander-dog)