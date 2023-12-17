# Персональный помощник для студентов
- Цель проекта:
> Облегчить студентам получение знаний из зарубежных источников, затрачивая на эти задачи минимум  времени.

- Функцианльность:
> Перевод статьи с английского языка на русский и генерация краткого тезисного конспект текста. 

## Начало работы
1. Инструкции по настройке окружения для скачивания и запуска проекта локально:
   *(Последовательно выполните на машине linux  следующие команды)*
- `$ mkdir имя_папки`  *создайте папку в которую вы поместите проект*
- `$ cd имя_папки`
- `$ sudo apt update`
- `$ sudo apt install python3.10-venv`
- `$ python3 -m venv venv_name` *Создайте новое окружение, где venv_name - название окружения*
- `$ source venv_name/bin/activate`
  
1.2. Импорт и запуск  проекта:
- `$ git clone git@github.com:<you-info>.git` *(Сколнируйте проект в созданную вами папку)*
- `$pip install -r requirements.txt` *(Установите зависимости из файла)*
- `$python manage.py runserver` *(Запустите приложение)*
- Перейдите по адресу:  http://127.0.0.1:8000/ в браузере

## Использование
1. Перейдите на главную страницу приложения **Home**;
2. Втсавьте в поле **Текст ситатьи** нужный для перевода текст и нажмите на конопку **Translate**;
   > В поле **Перевод статьи** отобразится переведдный на русский язык текст.
3. Нажмите на кнопку **summary** для генерации краткого содкржания статьи;
   > Краткое изложение сатьи отобразится в поле **Краткое содержание статьи**.

## Команда
- Менеджер проекта - Попова И.К.
- Аналитик данных - Максимова Н.В.
- Инженер по машинному обучению - Запатоцкий Юрий М.
- Full Stack разработчик - Сергеев Владимир В.
- Тестировщик QA инженер - Андрей
- Документалист - Рагимов А.Ю.

## Лицензия
Приложение включает в себя код из библиотеки Python, Django, Pandas, Numpy, Transformers, Hugging face, Bootstrap.
Все компоненты входящие в состав приложения с открытым исходным кодом и имеют разрешающаю лицензия GPL.
