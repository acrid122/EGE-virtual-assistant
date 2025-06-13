# EGE Virtual Assistant
Виртуальный помощник для подготовки к ЕГЭ по информатике.

## Установка
1. Установите Docker и Docker Compose.
2. Склонируйте репозиторий: `git clone https://github.com/acrid122/EGE-virtual-assistant.git`
3. Создайте `.env` на основе `.env.example`.
4. Запустите: `docker-compose up --build`

## Тестирование
- БД: `pytest backend/tests/test_db.py`
- Redis: `pytest backend/tests/test_redis.py`
- Celery: `pytest worker/tests/test_celery.py`

## Стек
- Frontend: React (Telegram Web App)
- Backend: Flask, Postgres, Redis, Celery
- Avatar: facexlib, VToonify, Wav2Lip, SadTalker, Coqui TTS
- Хранилище: Yandex S3
- Мониторинг: Prometheus