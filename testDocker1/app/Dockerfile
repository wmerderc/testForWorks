# Используем официальный образ Python
FROM python:3.9

# Устанавливаем зависимости
RUN pip install Flask pymongo

# Копируем приложение в контейнер
COPY . /app

# Устанавливаем рабочую директорию
WORKDIR /app

# Запускаем приложение
CMD ["python", "app.py"]
