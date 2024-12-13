# Genetic Tests API

API для управления данными генетических тестов животных.

## Запуск проекта

1. Клонируйте репозиторий
2. Запустите проект с помощью Docker:
```bash
docker compose up --build
```

После запуска сервер будет доступен по адресу: http://localhost:8000

## API Endpoints

Базовый URL: `http://localhost:8000/api`

### 1. Добавление данных генетического теста
```http
POST /api/tests/

{
    "animal_name": "Буренка",
    "species": "корова",
    "test_date": "2023-11-18",
    "milk_yield": 28.5,
    "health_status": "GOOD"
}
```

### 2. Получение списка всех тестов
```http
GET /api/tests/
```

### 3. Фильтрация по виду животного
```http
GET /api/tests/?species=корова
```

### 4. Получение статистики
```http
GET /api/statistics/
```

## Документация API

Swagger документация доступна по адресу:
```http
GET /api/docs/
```

Схема API в формате OpenAPI:
```http
GET /api/schema/
```

## Примеры ответов

### Статистика
```json
{
    "statistics": [
        {
            "species": "корова",
            "total_tests": 1,
            "avg_milk_yield": 28.5,
            "max_milk_yield": 28.5,
            "good_health_percentage": 100
        }
    ]
}
```

## Остановка проекта

Для остановки проекта выполните:
```bash
docker compose down
```

Для полной очистки данных (включая базу данных):
```bash
docker compose down -v
```