
# Upload-Service

REST API сервис для загрузки и хранения файлов (DICOM, PNG, JPG, PDF) с использованием FastAPI, MinIO и PostgreSQL.

## Возможности

- Загрузка файлов через эндпоинт `/upload`
- Сохранение файлов в MinIO
- Авторизация через JWT (Bearer Token)
- Сохранение метаданных в PostgreSQL (имя, размер, путь)

## Быстрый запуск

1. Перейдите в директорию проекта:
```bash
cd upload_project
```

2. Соберите и запустите сервис:
```bash
docker-compose up --build
```

3. Откройте документацию API в браузере:
```
http://localhost:8000/docs
```

## Данные по умолчанию

### PostgreSQL
- Хост: localhost
- Порт: 5432
- Пользователь: postgres
- Пароль: 1234
- База данных: upload_db

### MinIO
- Веб-интерфейс: http://localhost:9001
- Access Key: minioadmin
- Secret Key: minioadmin
- Название бакета: uploads

## Пример запроса через curl

```bash
curl -X POST http://localhost:8000/upload   -H "Authorization: Bearer <ваш_jwt_токен>"   -F "file=@/путь/к/файлу.pdf"
```

## Пример запроса в Postman
- Метод: POST
- URL: http://localhost:8000/upload
- Заголовки:
  - Authorization: Bearer <ваш_jwt_токен>
- Тело запроса:
  - Тип: form-data
  - Ключ: file
  - Значение: файл для загрузки

## Зависимости (requirements.txt)

Файл `requirements.txt` содержит список всех библиотек, используемых в проекте. Убедитесь, что он сохранён в кодировке UTF-8.

## Тестирование

Пример юнит-теста (`tests/test_upload.py`):
```python
def test_upload_success():
    # Проверка успешной загрузки файла
    ...
```

## Возможные улучшения

- Ограничение размера файлов
- Использование хэш-суммы как идентификатора
- Приватный доступ к MinIO с временными ссылками
- Валидация содержимого DICOM-файлов

## Заключение

После запуска вы можете загружать файлы через API с авторизацией. Убедитесь, что MinIO и база данных работают корректно.
