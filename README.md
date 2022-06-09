# test_case

Создать виртуальное окружение python3.10, pip install -r requirements.txt

python manage.py runserver 0.0.0.0:8000

curl --request GET --url http://127.0.0.1:8000/ --header 'Authorization: Bearer 1cc53254c9b7b8af6ef9167b84ee44f34ae21dba'
  
В базе единственный пользователь admin с токеном, указанным выше в запросе

Для создания нового пользователя (с автоматическим присвоением токена) можно запустить скрипт: python manage.py create_user

Также, демопроект развернут на vds сервере (формат запроса аналогичен): http://162.19.131.80/
