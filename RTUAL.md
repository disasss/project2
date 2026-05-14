# Виртуальное окружение для проекта **project2**

Виртуальное окружение (virtualenv / `venv`) — это отдельная копия Python и пакетов для проекта. Так вы не смешиваете зависимости сайта с системными и можете зафиксировать версии из `requirements.txt` (у нас: Django 6.0.4, WhiteNoise, Waitress, Pillow).

Ниже — три типичных сценария: **Windows (PowerShell)**, **PythonAnywhere** (как в оригинальной инструкции) и **как указать venv в веб-приложении**.

---

## Шаг 1. Создать окружение

### Windows (рекомендуется для этой лаборатории)

В каталоге проекта (где лежит `manage.py` и `requirements.txt`):

```powershell
cd C:\Users\LenovoLOQ\Downloads\project2
python -m venv venv
```

Версия `python` должна быть той же, с которой потом запускаете сайт (например 3.12). Проверка:

```powershell
python --version
```

### PythonAnywhere (Bash + virtualenvwrapper)

На вкладке **Consoles** откройте **Bash**. Убедитесь, что версия Python совпадает с той, что выбрана для веб-приложения (например 3.10):

```bash
mkvirtualenv project2 --python=/usr/bin/python3.10
```

После создания в приглашении появится префикс `(project2)`.

Если команда `mkvirtualenv` не найдена — установите virtualenvwrapper по [документации PythonAnywhere](https://help.pythonanywhere.com/pages/InstallingVirtualenvWrapper/).

---

## Шаг 2. Активировать окружение и установить пакеты

### Windows

```powershell
.\venv\Scripts\Activate.ps1
```

Проверка, что используется Python из venv:

```powershell
where python
pip --version
```

Установка зависимостей проекта:

```powershell
pip install -r requirements.txt
```

### PythonAnywhere

```bash
workon project2
which pip
pip install -r /home/ВАШ_ЛОГИН/project2/requirements.txt
```

(Замените путь на реальный путь к клону проекта на PythonAnywhere.)

---

## Шаг 3. Настроить приложение на использование этого venv

### Локально (Windows)

Ничего отдельно «прописывать» в Django не нужно: вы просто всегда запускаете команды **после** `Activate.ps1`, тогда `python` и `pip` берутся из `venv`.

Пример:

```powershell
.\venv\Scripts\Activate.ps1
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Production через Waitress — см. `DEPLOY_WINDOWS.md` (перед запуском задайте `DJANGO_ALLOWED_HOSTS`).

### PythonAnywhere (вкладка Web)

1. Откройте **Web** → ваше приложение.
2. В разделе **Virtualenv** укажите путь к окружению, например:

   `/home/ВАШ_ЛОГИН/.virtualenvs/project2`

   Если используете virtualenvwrapper, часто достаточно ввести имя окружения: `project2` — система подставит путь к `~/.virtualenvs/...`.
3. В **WSGI configuration file** должен указываться модуль `project2.wsgi` (как в ручной настройке Django).
4. Нажмите **Reload** веб-приложения.

После перезагрузки приложение использует пакеты из указанного venv, а не системные.

---

## Деактивация и повторная активация

### Windows

```powershell
deactivate
```

Снова включить:

```powershell
.\venv\Scripts\Activate.ps1
```

### PythonAnywhere

```bash
deactivate          # выйти из venv
workon project2 # снова войти
```

---

## Краткая шпаргалка по проекту **project2**

| Действие              | Команда (после активации venv)        |
|-----------------------|----------------------------------------|
| Установить зависимости| `pip install -r requirements.txt`      |
| Миграции              | `python manage.py migrate`             |
| Статика               | `python manage.py collectstatic`       |
| Локальный сервер      | `python manage.py runserver`           |

Файл зависимостей в корне проекта: `requirements.txt`.
