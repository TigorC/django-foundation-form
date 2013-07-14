#!/usr/bin/env python
from django.conf import settings
from django.core.management import call_command


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=('foundationform',),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':MEMORY:',
            }
        },
    )

if __name__ == "__main__":
    call_command('test', 'foundationform')
