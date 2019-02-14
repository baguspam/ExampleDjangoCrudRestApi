Example Crud Django Admin dengan Django Rest Framework

Step instalasi :
- Git clone dulu repositorynya
- Install Python 3.7.1
- Download Visual Studio Code + install plugin Django
- Open project
- New terminal ->
  python -m venv env
  env\Scripts\activate.bat
  pip install -r requirements.txt
  python manage.py runserver
  username: admin && password: admin
- Jika tidak bisa login
  python manage.py createsuperuser
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver

Link cek rest api
- 127.0.0.1:8000/api/buku
- 127.0.0.1:8000/api/mahasiswa
- 127.0.0.1:8000/api/pinjam