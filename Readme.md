Change your models (in models.py).
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.

python manage.py sqlmigrate polls 0001 # Returns what will the migration do in SQL format
python manage.py check # checks for any problems in the project

python manage.py createsuperuser # creates an admin user
 http://127.0.0.1:8000/admin/ # url of the admin site

python manage.py runserver

note : "pools" folder should be named pools_api
since the app holds all the api.

using DRF, more infos here : https://www.django-rest-framework.org/tutorial/quickstart/

packages : djangorestframework, PyJWT, django-cors-headers, django-environ
