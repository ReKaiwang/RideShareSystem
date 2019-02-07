To run our project:
1. check your python version which should be python 3.6 or larger
2. python manage.py makemigrations ride_request user (if you haven't migration or model has been changed)
3. python manage.py migrate (check whether the model has been changed)
4. python manage.py runserver 8000

Remainder: 
1. The database for the project has been set up and it has three test usrs for the project
2. superusers username: programmer password: programmer
3. If you want to restart the project, please delete file db.sqlite3 and directory users/migrations and ride_request/migrations 