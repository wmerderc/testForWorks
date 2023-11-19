import requests

url = "http://127.0.0.1:5000/get_form"

# Примеры данных для тестирования
test_data = [
    {
        "email": "test@example.com",
        "phone": "+79953847890",
        "date": "01.01.2022",
        "text": "Hello, World!"
    },
    {
        "email": "test@example.com",
        "phone": "1234567890",
        "date": "01.01.2022",
        "text": "Hello, World!"
    },
    {
        "email": "testexample.com",
        "phone": "1234567890",
        "date": "01.01.2022",
    },
    {
        "date": "01.01.2022",
        "text": "Hello, World!"
    },
    {
        "email": "test@example.com",
        "phone": "+79953846759",
        "date": "2022-01-22",
        "text": "Hello, World!"
    },
    {
        "email": "test@example.com",
        "phone": "1234567890",
        "date": "01.01.2022",
        "text": "Hello, World!"
    },
    {
        "phone": "+79529846848",
        "text": "Hello, World!"
    },
    {
        "texewt": "Hello, World!"
    },
    {
        "email": "test@example.com",
        "text": "Hello, World!"
    },
    {
        "emaiewrl": "test@example.com",
        "text": "Hello, World!"
    },
    {
        "text": "Hello, World!"
    },
    {
        "email": "test@example.com",
        "phone": "+79189631789",
    },
    {
        "email": "test@example.com",
        "phone": "1234567890",
        "date": "01.01.2022",
        "text": "Hello, World!"
    }
]

for data in test_data:
    response = requests.post(url, params=data)
    print(f"Response: {data}\nResult: {response.json()}\n")
