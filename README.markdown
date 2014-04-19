# django\_min

Proof-of-concept that Django doesn't *need* massive amounts of boilerplate to
function.

A hello world `app.py`:

```python
from django.conf.urls import patterns, url
from django.http import HttpResponse

## VIEWS ##

def index(request):
    return HttpResponse('Hello, world')

## ROUTES ##

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
)
```

Minimal `settings.py`:

```python
# Optional: debug mode
DEBUG = True
TEMPLATE_DEBUG = True

# Location of routes (main app.py file)
ROOT_URLCONF = 'app'

# Secret key is required by Django
SECRET_KEY = 'r*ll9mlx=d)cko4gp03ms%+tmq51+dlyo06gl2$xbt$w=7$=_8'
```

Generated `manage.py`:

```python
#!/usr/bin/env python
import os, sys
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
```

Install Django. To use a [virtual
environment](http://www.virtualenv.org/en/latest/virtualenv.html) in Python
3.4, use these commands:

    python3.4 -mvenv .
    bin/pip install -r requirements.txt

Then run with:

    bin/python manage.py runserver
