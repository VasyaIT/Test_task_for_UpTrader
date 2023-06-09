﻿# Test_task_for_UpTrader
Этот проект для компании UpTrader

Это мини-приложение с древовидным меню

Объекты для этого меню берутся из базы данных

Перед клонированием репозитория внимательно прочитайте README.md!!!


## Requirements
* Django==4.2
* flake8==6.0.0
* pre-commit==3.2.2
* sqlparse==0.4.4
* tzdata==2023.3
* pycodestyle==2.10.0
* pyflakes==3.0.1
* python-dotenv==1.0.0

Django-mmpt не используется! Это запрещено в задании  (остальные зависимости - это линтеры и т.д)

## Прошу внимательно ознакомится с настройками
![Image db](https://github.com/VasyaIT/Test_task_for_UpTrader/blob/main/db.png)

Здесь используется PostgreSQL, но по умолчанию из переменной окружения берутся настройки SQLite3

Поэтому, если хотите использовать SQLite, то можете ничего не трогать

# Установка

Первым делом клонируйте этот репозиторий

```commandline
git clone git@github.com:VasyaIT/Test_task_for_UpTrader.git
```
Далее создайте виртуальное окружение и активируйте его (в каждой операционной системе это делается немного по-разному)

Установите зависимости
```commandline
pip install -r req.txt
```
Зависимости могут установится не все из-за legacy ошибки

### После этого обязательно запустите миграции и создайте суперпользователя, потому что базы данных не будет
Но для начала перейдите в директорию проекта
```commandline
cd .\tree_menu\ 
```
```commandline
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
```
### Запустите локальный сервер
```commandline
python3 manage.py runserver
```

Добавлять меню можно много и без разницы, как оно будет называться

Все меню выводятся на одной странице
