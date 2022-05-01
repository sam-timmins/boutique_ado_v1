
* Install django
```
pip3 install django==3.2
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

* Copy the allauth templates into the allauth folder
```
cp -r ../.pip-modules/lib/python3.8/site-packages/allauth/templates/* ./templates/allauth/
```

* Delete the folder
    * tests
    * openid

* Create a base.html file in the templates directory and begin creating

```html
{% load static %}

<!doctype html>
<html lang="en">
  <head>
    {% block meta %}
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    {% endblock %}

    {% block extra_meta %}
    {% endblock %}

    {% block corecss %}
    {% endblock %}

    {% block extra_css %}
    {% endblock %}

    {% block corejs %}
    {% endblock %}

    {% block extra_js %}
    {% endblock %}

    <title>Boutique Ado {% block title %}{% endblock %}</title>
  </head>
  <body>

    <header class="container-fluid fixed-top"></header>

    {% if messages %}
        <div class="message-container"></div>
    {% endif %}

    {% block page_header %}
    {% endblock %}

    {% block content %}
    {% endblock %}

    {% block postloadjs %}
    {% endblock %}

  </body>
</html>
```

* Create a home app
```
python3 manage.py startapp home
```

* Create a templates directory in the home app
```
 mkdir -p home/templates/home
```

* Create an index.html file in the home folder
```html
{% extends "base.html" %}
{% load static %}

{% block content %}
    <h1 class="display-4 text-success">It works!!</h1>
{% endblock %}
```

* Create a view to render the template
```py
from django.shortcuts import render

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

```

* Create a urls.py file and add...
```
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]

```

* Change TEMPLATES in settings.py to 

```py
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
```

* Add the home app to installed app in settings.py

* Create new folders....
```
mkdir static
```

```
mkdir static/css
```

```
mkdir media
```

* Add the file paths to settings.py
```py
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

* In the project urls.py

```py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # add this
from django.conf.urls.static import static # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add this
```


# Stripe

install stripe and freeze requirements

```
pip3 install stripe
```

Add script tag to base.html
```html
<script src="https://js.stripe.com/v3/"></script>
```

In the checkout page, 

```html
<!-- Give form an id of 'payment-form' and submit button an id of 'submit-button' -->
<!-- Add 2 divs in form -->
    <!-- A Stripe card element will go here -->
    <div class="mb-3" id="card-element"></div>

    <!-- Used to display form errors -->
    <div class="mb-3 text-danger" id="card-errors" role="alert"></div>

<!-- Add script tags -->
{% block postloadjs %}
    {{ block.super }}
    {{ stripe_public_key|json_script:"id_stripe_public_key" }}
    {{ client_secret|json_script:"id_client_secret" }}
    <script src="{% static 'custom script file here' %}"></script>
{% endblock %}
```

In the script tag from above

```js

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);

//  Sets up stripe
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

// Styles for stripe inputs
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};


var card = elements.create('card', {style: style});
// Mount the card to the div in the template
card.mount('#card-element');

// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fa-solid fa-bomb"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});
```

*See css file for stripe's css*

In main settings.py

```py
# Prevent error when hidden env.py is not found
if os.path.isfile('env.py'):
    import env

STRIPE_CURRENCY = 'GBP'
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
```

In env.py
```py
os.environ['STRIPE_PUBLIC_KEY'] = 'Key from stripe dashboard here'
os.environ['STRIPE_SECRET_KEY'] = 'Key from stripe dashboard here'
```

```py

import stripe

# Import the context file to access the grand_total
from bag.contexts import bag_contents
# Import the main settings file for accessing the stripe public and secret keys
from django.conf import settings

def checkout(request):
    # Set the public and secret keys
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    # The grand total rounded and set to an integer
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    #  Set the secret key
    stripe.api_key = stripe_secret_key

    #  Error message if the public key is missing
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    #  Create payment intent
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        )

    #  Add keys to context for the template
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
```


