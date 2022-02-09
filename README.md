# mediasoft

Ушeнин Юpий

## Тестовое задание Python
Данный репозиторий содержит выполненное тестовое задание.

## Описание проекта
Django, Django REST framework.
Запускается 3 контейнера

- mediasoft_nginx - контейнер с nginx
- mediasoft_web - приложение Django REST framework
- mediasoft_db - база данных PostgreSQL

## Подготовительные действия
Установка:
1. git
2. docker
3. docker-compose

## Как запустить

1. Клонируем репозиторий

    ```bash
    git clone git@github.com/yuriyur/mediasoft.git
    ```

2. Собираем и запускаем докер контейнеры в фоновом режиме

    ```bash
    docker-compose up --build -d
    ```

3. Выполняем миграцию базы данных

    ```bash
    python manage.py makemigrations 
    ```
    ```bash
    python manage.py migrate
    ```
## Использование

- http://localhost/api/v1/city/ - все города 
- http://localhost/api/v1/city/create - создать город
- http://localhost/api/v1/city/street - все улицы
- http://localhost/api/v1/city/street/create - создать улицу
- http://localhost/api/v1/city/1/street - фильтр улиц по городу 
- http://localhost/api/v1/shop/ - все магазины
- http://localhost/api/v1/shop/create - создать магазин
- http://localhost/api/v1/shop/edit/1/ - редактировать магазин
- http://localhost/api/v1/shop/?street=1&city=1&open=1 - фильтр магазинов
