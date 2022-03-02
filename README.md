
* Install django
```
pip3 install django==3.2 gunicorn
```

* Create a project
```
django-admin startproject PROJECT_NAME .
```

* Add to the .gitignore file
```
*.sqlite3
*.pyc
```

* Migrate files
```
python3 manage.py migrate
```

* Create superuser
```
python3 manage.py createsuperuser
```

* Install allauth
```
pip3 install django-allauth==0.41.0
```

* From the allauth [documentation](https://django-allauth.readthedocs.io/en/latest/installation.html) Copy in...
```py
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
```

* To installed apps add...
```py
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
```

* Under the AUTHENTICATION_BACKENDS add...
```py
SITE_ID = 1
```

* Add allauth urls to project ulrs file
```py
path('accounts/', include('allauth.urls')),
```

* And add the import of include
```py
from django.urls import path, include
``` 

* Migrate files
```
python3 manage.py migrate
```

* Run the application
```
python3 manage.py runserver
```

* Login as admin and open the *Sites* link and update
    * Domain name to *project_name.example.com*
    * Display name to the *project name*