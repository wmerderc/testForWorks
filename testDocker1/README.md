# Проект Flask с MongoDB и Docker Compose

Этот проект представляет собой простой пример того, как настроить веб-приложение на Python Flask с использованием MongoDB, используя Docker Compose.

## Требования

Прежде чем начать, убедитесь, что у вас есть следующее:

- Docker: [Установить Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Установить Docker Compose](https://docs.docker.com/compose/install/)

## Начало работы

1. **Клонируйте**: 
    ```    
    git clone https://github.com/ваш-пользователь/flask-mongodb-docker-compose.git
    cd flask-mongodb-docker-compose
2. **Создание и запуск контейнеров**:
    Используйте Docker Compose, чтобы создать и запустить контейнеры. Это настроит приложение Flask и MongoDB.
    ```
    docker-compose up
3. **Доступ к веб-приложению**:
    После запуска контейнеров вы можете получить доступ к веб-приложению Flask в вашем веб-браузере.
    URL:  http://localhost:8080

4. **Использование API**:
    Веб-приложение Flask предоставляет простой API с тремя точками доступа для создания, обновления и чтения значений в MongoDB.
    Создание значения:
    ```
    POST http://localhost:8080/create
    Body: {"key": "мойключ", "value": "моевыражение"}
    
    ```
    Обновление значения:
    ```
    PUT http://localhost:8080/update/<id>
    Body: {"value": "новоезначение"}
    ```
    Чтение значения:
    ```
    GET http://localhost:8080/read/<id>
    ```
