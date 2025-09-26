# Django girls amsterdam

## Getting started using django

Initiate the project using `django-admin startproject <projectname> .`

Then within `settings.py` we can chane settings such as timezones. The important one is to add 

```py
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
```

Because of the deploying on (pythonanywhere)[https://pythonanywhere.com] we need a few more lines.

```py
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.pythonanywhere.com']
```

What this does is when we run our blog the destination URL is allowed to be a host.

We also need a secret-key. This is a random string sequence that gets used when a random injection is needed.

```bash
python -c 'from django.core.management.utils import get_random_secret_key; \
      print(get_random_secret_key())'
```

this new key can be retreived using `SECRET_KEY = os.getenv('SECRET')` and `import os`

We can now create the database using the command `python manage.py migrate`

## Running the app

`python manage.py runserver`

## Models

Models are an object. Objects have attributes. A ball has a pattern, colors, textures, sizes and more.

The model defines what a object has and how it is stored in our database.

Before we create our model we need to clean up the codebase.

`python manage.py startapp blog` creates a new app within our project. Apps can be seen as functions, managers or departments within an app. Once the features increase inside of a website you can create more apps to keep things organised. 

do not forget to add the new app in the `settings.py` `INSTALLED_APPS` variable.

### Migrations

When adding new functionality to a app the database might need to reflect new data. To add this data we make a database migration. This just specifies what has been changed with the new update. This is called a code first development approach. If something goes wrong and we need a older version of the database we can go back down the migrations.

We create a migrations using `python manage.py makemigrations blog` `python manage.py migrate blog`

## Creating a admin panel

goto `<app>/admin.py` and add

```py
from .models import Post

admin.site.register(Post)
```

Before we can access this admin panel we need to create a account. This is done using the command `python manage.py createsuperuser`.

## Deploying to pythonanywhere

Login to pythonanywhere and create a bash terminal.

Within this terminal run `pip install --user pythonanywhere` this will setup a variety of different things.

After this run `$ pa_autoconfigure_django.py --python=3.10 https://github.com/<your-github-username>/my-first-blog.git` to download your git repository.

Recreate a new super user and you can now access the admin panel of your site by visiting the url given by pythonanywhere (most likely <username>.pythonanywhere.com)