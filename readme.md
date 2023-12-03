Проект для создания рассылок.

Для запуска прокта нужно запустить сам проект Джанго с помощью команды:
python3 manage.py runserver

А также запустить сервер celery
celery -A config worker --beat -l info
