# nmea_web_app

1. Установить Django Framework:

  `pip install django`

2. Зайти папку с проектом.
3. Выполнить миграции:

  `django manage.py makemigrations`
  
  `django manage.py migrate`

4. Выполнить парс GPS-файла:
5. Положить файл в папку tmp (по умолчанию файл уже находится там).

6. Запустить django shell:

  `python manage.py shell`

7. Выполнить следующие команды:

  `from table.utils import *`
   
  `load_nmea()`

8. Выйти из shell
9. Запустить проект:

  `python manage.py runserver`

10. Перейти по ссылке в браузере (по умолчанию localhost:8000)
