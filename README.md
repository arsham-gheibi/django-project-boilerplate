## Django Project Boilerplate 🎁

Essential 🐳 Django Boilerplate files to start your Django Projects EZ as 🥧

## What Does this Django Project Boilerplate Includes?

1. Dockerized Settings for Both Production and Development Environments
2. Pre Configured Security Settings
3. Pre Configured Unittests
4. Pre Configured .env Settings
5. Minimal requirements for Any Django Project
6. Flake8 for Code Quality
7. Gitignore for Git
8. Clean and Ready to use for your Project

```sh
git clone https://github.com/arsham-gheibi/django-project-boilerplate.git
cd django-project-boilerplate
```

Make a New Virtual Environment and install requirements with poetry.

```sh
python -m venv env
source env/bin/activate
python -m pip install poetry
poetry install --no-root
```

make a .env file and put your Credentials on that file.

```sh
cp .env.sample .env
```

## The Credentials

1. DJANGO_SECRET_KEY
2. DJANGO_ALLOWED_HOSTS
3. DB_NAME
4. DB_USER
5. DB_PASSWORD
6. DB_HOST
7. DB_PORT

Then Go ahead and make your Django App

```sh
docker compose run --rm app sh -c 'python manage.py startapp <app_name>'
```

To run tests (code style and Unit Tests), run the following:

```sh
docker compose run --rm app sh -c 'python manage.py wait_for_db && python manage.py tests && flake8'
```

Happy Coding 🥳
