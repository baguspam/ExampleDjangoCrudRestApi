Example Crud Django Admin dengan Django Rest Framework


Step instalasi :
- Git clone dulu repositorynya
- Install Python 3.7.1
- Download Visual Studio Code + install plugin Django
- Open project
- New terminal ->
<br/>python -m venv env
<br/>env\Scripts\activate.bat
<br/>pip install -r requirements.txt
<br/>pip install gunicorn
<br/>pip install django-heroku
<br/>python manage.py runserver
<br/>username: admin && password: admin
- Jika tidak bisa login
<br/>python manage.py createsuperuser
<br/>python manage.py makemigrations
<br/>python manage.py migrate
<br/>python manage.py runserver

Link cek rest api:
<br/>- 127.0.0.1:8000/api/buku/
<br/>- 127.0.0.1:8000/api/mahasiswa/
<br/>- 127.0.0.1:8000/api/pinjam/
