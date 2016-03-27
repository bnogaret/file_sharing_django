# File sharing application

file_sharing_django is a small project to try / learn django.

## Features

1. manage users
2. manage groups of users
3. let them share files (PDF file)

## Technologies

### Server side

- [Python 3.5](https://www.python.org/): the language of choice
- [Django 1.9](https://www.djangoproject.com/): Python web framework
- [PostgreSQL 9.4](http://www.postgresql.org/): relational database, used to save django data (user account, sessions ...), files information

### Client side and design

## Installation

Install python 3.5 from [the website](https://www.python.org/downloads/release/python-351/). Make sure python is in the path environment.

I advice you to use a virtualenv to install the app ([for more information](http://docs.python-guide.org/en/latest/dev/virtualenvs/)).

### Python packages

Python 3.4 and later directly include pip, a python package manager. From inside the repository, run:

    pip install -r requirements.txt

Some of the packages installed by this command are not necessary to run file_sharing_django (such as pylint, pylint-django and pylint-common that are for code analysis). You can ignore them and install manually the essential packages.

## Handy links

- [django tutorial](https://docs.djangoproject.com/en/1.9/intro/)
- [Newsblur](https://github.com/samuelclay/NewsBlur): model for my app
