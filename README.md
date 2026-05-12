# Лабораторная работа №11

## Деплой Django-проекта на Windows

### Цель работы
Научиться подготавливать Django-проект к публикации и выполнять деплой веб-приложения на сервер.

## Выполненные настройки в проекте

- В `college_site/settings.py` установлено `DEBUG = False`.
- В `college_site/settings.py` задан `ALLOWED_HOSTS` через переменную окружения `DJANGO_ALLOWED_HOSTS`.
- Настроены статические файлы:
  - `STATIC_URL = '/static/'`
  - `STATIC_ROOT = BASE_DIR / 'staticfiles'`
- Добавлен файл зависимостей `requirements.txt`.

## Порядок деплоя (Windows)

### 1) Проверка локального запуска
```powershell
python manage.py runserver
```

### 2) Сбор статических файлов
```powershell
python manage.py collectstatic
```

### 3) Установка зависимостей
```powershell
pip install -r requirements.txt
```

### 4) Миграции и администратор
```powershell
python manage.py migrate
python manage.py createsuperuser
```

### 5) Запуск в production через Waitress
Перед запуском укажи IP/домен сервера в `DJANGO_ALLOWED_HOSTS`:

```powershell
$env:DJANGO_ALLOWED_HOSTS="127.0.0.1,localhost,192.168.1.98,your-domain.com"
```

Узнать IP сервера можно так:

```powershell
ipconfig
```

После этого запускай сервер:

```powershell
waitress-serve --host=0.0.0.0 --port=8000 college_site.wsgi:application
```

Открыть в браузере:

```text
http://IP_СЕРВЕРА:8000
или
http://your-domain.com
```

Если сайт не открывается из сети, открой порт 8000 в Windows Firewall.

```powershell
netsh advfirewall firewall add rule name="Django 8000" dir=in action=allow protocol=TCP localport=8000
```

Убедись, что на сервере используется запуск на всех интерфейсах:

```powershell
waitress-serve --host=0.0.0.0 --port=8000 college_site.wsgi:application
```

Проверка с другого устройства в этой же Wi‑Fi сети:

```text
http://192.168.1.98:8000
```

## Практический результат
После выполнения указанных шагов проект готов к деплою на Windows-сервере и доступен по IP-адресу/домену.
