## Django Project Boilerplate 🎁

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
```

Make a New Virtual Environment

```sh
python -m venv env
source env/bin/activate
python -m pip install -r requirements.txt
```

make a .env file and Put your Credentials on that file

```sh
touch app/.env
```

## The Credentials are :

1. ENVIROMENT (production or development)
2. SECRET_KEY
3. DOMAIN
4. DB_NAME
5. DB_USER
6. DB_PASSWORD
7. DB_HOST
8. DB_PORT

```sh
python manage.py migrate
python manage.py runserver
```

Then Go ahead and make your Project

```sh
python manage.py startapp <app_name>
```

Happy Coding 🥳
