# Test Task UpTrader
Тестовое задание: Реализация древовидного меню на Django.


## Стек технологий

- Python 3.12
- Django
- SQLite


## 🚀 Как запустить проект
1. Клонируйте репозиторий:
```bash
git clone https://github.com/Nikita-Makkar/test_task_UpTrader.git
cd test_task_UpTrader
```
2. Создайте и активируйте виртуальное окружение:

```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Установите зависимости:

```bash

pip install -r requirements.txt
```
4. Примените миграции:

```bash


python manage.py migrate
```
5. Запустите сервер:

```bash

python manage.py runserver
```
6. Создайте суперпользователя

```Bash
python manage.py createsuperuser
```

Перейдите в админку (/admin) и создайте элементы меню.


🛠 Как использовать
Создайте меню и пункты меню в админке Django.

Вставьте тег {% draw_menu 'название_меню' %} в нужный шаблон.

Пункты меню автоматически будут подсвечиваться в зависимости от текущего URL.


🔧 Стек технологий
Python 3.12

Django 5.2

Только стандартная библиотека Python

Автор

``Nikita Makkar``