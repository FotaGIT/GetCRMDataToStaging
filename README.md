# GetCRMDataToStaging Project Readme.md File 

End of line application

The clean, fast and right way to start a new Django `4.1` powered website.

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r requirements.txt


$ cd project/
$ python manage.py migrate
$ python manage.py runserver
```

## Step

1. python -m virtualenv venv.
2. wfastcgi-enable # for iis
3. if database schema
   ```
   drop schema public cascade;
   create schema public;
   ```


