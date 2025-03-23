import os

assert (
    os.environ['SERVER_ENV'].lower() == 'local' and
    os.environ['DB_HOST'].lower() in ['localhost', '127.0.0.1']
), \
    'This script should be run in local dev mode only with local postgres.'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "home.settings")
print("Django settings module home.settings")

import django

django.setup()

print("Django setup done.")
