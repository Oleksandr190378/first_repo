FROM python:3.11-slim

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

COPY pyproject.toml  $APP_HOME/pyproject.toml
COPY poetry.lock  $APP_HOME/poetry.lock

# Встановимо залежності всередині контейнера
RUN pip install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install --only main

# Скопіюємо інші файли в робочу директорію контейнера
COPY . .

# Запустимо наш застосунок всередині контейнера
ENTRYPOINT ["python", "helper_bot/main.py"]