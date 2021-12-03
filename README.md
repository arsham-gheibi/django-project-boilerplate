## Django Project Boilerplate

a Simple Django Boilerplate to Starting your django Projects EZ as 🥧

## What Does this Django Project Boilerplate Includes ?

1. Settings for Both Production and Development Environments
2. Pre Configured Security Settings
3. Pre Configured .env Settings
4. Minimal requiremnts for Any Django Project
5. Flake8 for Code Quality
6. Gitignore for Git
7. Clean and Ready to use for your Project

```sh
git clone https://github.com/SeelpAydin/django-project-boilerplate.git
cd django-project-boilerplate
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

make a .env file and Put your Credentials on that file

```sh
touch app/.env
```

The Credentials are :

ENVIROMENT=
SECRET_KEY=
DOMAIN=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=

```sh
python manage.py migrate
python manage.py runserver
```
