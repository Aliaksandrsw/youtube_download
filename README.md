# YouTube Загрузчик и Конвертер

Это приложение на Django позволяет пользователям скачивать видео с YouTube или конвертировать их в формат MP3. 
Приложение упаковано в Docker для удобства развертывания и запуска.

## Функции

- Скачивание видео с YouTube
- Конвертация видео YouTube в MP3


## Используемые технологии

- Python 3.x
- Django 5.0.7
- yt-dlp 2024.7.9
- PostgreSQL (в качестве базы данных)
- Docker и Docker Compose

## Требования

- Docker
- Docker Compose
- FFmpeg

## Установка FFmpeg

Перед запуском приложения убедитесь, что FFmpeg установлен на вашей системе.

### На Ubuntu/Debian:
sudo apt update
sudo apt install ffmpeg

### На macOS (с использованием Homebrew):
brew install ffmpeg

### На Windows:

#### Использование Chocolatey 
1. Установите Chocolatey, если он еще не установлен. Инструкции можно найти на [официальном сайте Chocolatey](https://chocolatey.org/install).
2. Откройте командную строку или PowerShell от имени администратора.
3. Выполните команду:  choco install ffmpeg
4. После установки перезапустите командную строку или PowerShell.

## Установка и запуск

1. Клонируйте репозиторий: git clone https://github.com/Aliaksandrsw/youtube_download
2. Скопируйте файл `.env.example` и переименуйте его в `.env`:
3. Отредактируйте файл `.env`, заполнив его своими данными:
SECRET_KEY=ваш_секретный_ключ
DATABASE_ENGINE=django.db.backends.{ваша СУБД}
DATABASE_NAME=имя базы данных
DATABASE_USER=юзер
DATABASE_PASSWORD=ваш пароль
DATABASE_HOST=ваш db хост
DATABASE_PORT=ваш db порт
4. Запустите приложение с помощью Docker Compose: docker-compose up --build
5. Откройте браузер и перейдите по адресу `http://localhost:8000` (или другой порт, если вы изменили его в Docker Compose).
