# 💀 Jack    

A Django 3 and Bootstrap 5 based skeleton project

## 🔑 Passwords & Keys   

Passwords and secrets are not stored in the repo.  Copy jack/config.ini.example to jack/config.ini and update as needed.  A secret key can be generated with:

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

## 🗂️ Import Initial Data

Run the following to set up some sample help text:

```
python manage.py loaddata help.json
```

## 🧪 Testing  

Run test with the following command:

```
coverage run --source='.' manage.py test --parallel
```

To see the coverage run `coverage html` and then open `htmlcov/index.html` to see the report.

## 🤖 Cron jobs  

### 🆑 Clear sessions

```
0 1 * * * (/path/to/.env/jack/bin/python /var/www/website.com/manage.py clearsessions >> /var/www/website.com/logs/clear_sessions.log 2>&1)
```

### 📧 Mailer  

```
* * * * * (/path/to/.env/jack/bin/python /var/www/website.com/manage.py send_mail >> /var/www/website.com/logs/cron_mail.log 2>&1)
0,20,40 * * * * (/path/to/.env/jack/bin/python /var/www/website.com/manage.py retry_deferred >> /var/www/website.com/logs/cron_mail_deferred.log 2>&1)
0 0 * * * (/path/to/.env/jack/bin/python /var/www/website.com/manage.py purge_mail_log 7 >> /var/www/website.com/logs/cron_mail_purge.log 2>&1)
```

## 📦 Upgrade pip Packages  

```
pip list --outdated --format=freeze | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```
