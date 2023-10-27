import psutil
import requests
import time

# Задайте пороговое значение потребления памяти.
memory_threshold = 500000000  # 500 МБ

# URL для отправки HTTP-запроса.
api_url = "https://localhost/api/alarm"

# Пауза перед следующей проверкой.
sleep_time = 300

while True:
    # Получаем информацию о потреблении памяти
    memory_info = psutil.virtual_memory()

    # Проверяем, превышает ли потребление памяти порог
    if memory_info.used > memory_threshold:
        data = {
            "message": "Потребление памяти превысило порог",
            "memory_used": memory_info.used
        }
        try:
            response = requests.post(api_url, json=data)
            if response.status_code == 200:
                print("Запрос успешно отправлен")
            else:
                print(f"Ошибка при отправке запроса. Код состояния: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при отправке запроса: {str(e)}")

    time.sleep(sleep_time)
