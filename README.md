# test_case

Создать виртуальное окружение python3.10, pip install -r requirements.txt

python manage.py runserver

curl --request GET \
  --url http://127.0.0.1:8000/test_case \
  --header 'Authorization: Bearer 1cc53254c9b7b8af6ef9167b84ee44f34ae21dba'
  
В базе единственный пользователь admin с токеном, указанным выше в запросе

Для создания нового пользователя можно запустить скрипт: python manage.py create_user

