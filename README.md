
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

* In settings.py 
```py
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/success'
```

* Run the application and add /accounts/login to the url to attempt to login, it should redirect to the verify email page.

* Login as the superuser and in Email Addresses change the email to verified and primary

* Logout and try login in again, the 404 error should show *Request URL:	http://localhost:8000/*

* Freeze requirements
```
pip3 freeze > requirements.txt
```

* Create templates directory
```
mkdir templates
```

* Create allauth folder in templates directory
```
mkdir templates/allauth
```



