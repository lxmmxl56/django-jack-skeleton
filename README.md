# Jack

A Django-based skeleton

## To run

The initial commit is just a basic Django project created using the `startproject` command using the latest stable version of Django, currently version 3.1.7.

The only change is moving the secret key into a config.ini file that can be copied from jack/config.ini.example and then replaced with a proper key:

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
