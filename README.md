# Jack

A Django 3 and Bootstrap 5 based skeleton project

## Passwords & Keys

Passwords and secrets are not stored in the repo.  Copy jack/config.ini.example to jack/config.ini and update as needed.  A secret key can be generated with:

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
