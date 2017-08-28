# Students Attendance Tracking Service

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Coverage](https://img.shields.io/badge/coverage-52%25-yellow.svg)](https://github.com/kmike/django-coverage)

<br>
# Quick links

- [**Overview**](#overview)
- [**Demo**](#demo)
- [**Functional**](#functional)
- [**Technical Stack**](#technical-stack)
- [**Features**](#features)
- [**Installation**](#installation)
- [**Source**](#source)
- [**Author**](#author)


# Overview

### This service tracking the attendance of your students via web &nbsp;&nbsp; :busts_in_silhouette: :eyes: 


# Demo

### Do you want to see this project in action? [Visit it!](http://104.236.69.146/)


# Functional

### Available functions depends by rights of visitor:

#### *Anonimous rights*

- site language selection
- social login (automatically register as User after login)
- register on site (becomes User after email confirmation)
- view all students in one list
- bidirectional ordering of students on columns

#### *User rights*

- site language selection
- standard/social login
- CRUD students/groups
- enroll students into groups
- specify group leader
- mark attendance of students in journal
- filtering students by selected group
- bidirectional ordering of students/groups on columns
- edit his profile
- reset/change his password

#### *Spec User rights (permission is added by Administrator)*

- all User rights
- view actions log
- send letter to Administrator

#### *Administrator rights*

- overlord has all rights


# Technical Stack

- Ubuntu 14.04, Python 2.7.6, MySQL 14.14 Distrib 5.5.47
- Git 1.9.1, PIP 1.5.4, Virtualenv 1.11.4, 
- Django 1.7.11, Twitter Bootstrap 3.3.6, jQuery 1.11.3


# Features

### Development and Production modes

- Bootstrap Responsive Web Design allows working on any device
- English/Ukrainian language selection on site (I18N/L10N)
- Access to functionality, based on the visitors rights
- 2-step [customized](stud_auth/views.py) user registration on site with [Registration Redux](http://django-registration-redux.readthedocs.io/en/latest/)
- Standard and Social (Facebook) login, reset/change password support 
- User profile use User model extended by [additional fields](stud_auth/models.py)
- [AJAX mode](students/static/js/main.js) for all requests on site (page reload is absent)
- Browser History for AJAX mode with navigation in AJAX mode
- All forms are Bootstrap Modal and [Crispy Forms](http://django-crispy-forms.readthedocs.io/en/latest/)
- Captcha in login, registration, password reset and send letter forms
- Remember selected language and selected group in [cookies](https://plugins.jquery.com/cookie/)
- Pagination and bidirectional ordering of all lists by columns
- Use [widget](http://eonasdan.github.io/bootstrap-datetimepicker/) for input date in User profile and Student profile
- Custom widget for view photo in User profile and Student profile
- Customized logging system for write specified events to .log file
- Custom [signals](students/signals.py) for logging actions and tracking errors by email
- Customized [Admin interface](stud_auth/admin.py) for user profile additional fields
- Customized [Admin interface](students/admin.py) for students search, filter, edit, validation
- Custom context processors for [origin](studentsdb/context_processors.py) and [groups](students/context_processors.py) variables
- Custom tag [pagenav](students/templatetags/pagenav.py) display page navigation for only given list of objects
- Custom filter [str2int](students/templatetags/str2int.py) convert input string into integer. If impossible return 0
- Custom filter [nice_username](students/templatetags/nice_username.py) return user full name if exist, else username.  
Additionally, wrapping by `*` for staff, by `**` for superuser

### Development mode only

- Custom middleware [DBTimeMiddleware](studentsdb/middleware.py) display DB queries count and time
- Custom middleware [RequestTimeMiddleware](studentsdb/middleware.py) display request time
- Custom commands [stcount](students/management/commands/stcount.py) prints number of specified objects in a DB
- Custom commands [filldb](students/management/commands/fill_db.py) creates specified number (1..10) of objects in DB
- Custom commands [localize_static](students/management/commands/localize_static.py) set static to online/offline usage mode


# Installation

### Dependencies

```sh
$ sudo apt-get install python-dev libxml2-dev libxslt-dev libfreetype6-dev libjpeg8-dev zlib1g-dev
```

### PIP, Virtualenv and Git (if not installed)

```sh
$ sudo apt-get install pip==1.5.4 virtualenv==1.11.4 git==1.9.1
```

### MySQL (if not installed)

```sh
$ sudo apt-get install mysql-server mysql-client libmysqlclient-dev
$ sudo mysql_install_db
$ sudo /usr/bin/mysql_secure_installation
```

### Create DB and DB-User

```sql
$ mysql -u root -p
mysql> CREATE DATABASE students_db CHARACTER SET utf8 COLLATE utf8_general_ci;
mysql> CREATE USER "students_db_user"@"localhost" IDENTIFIED BY "password";
mysql> GRANT ALL PRIVILEGES ON students_db.* TO "students_db_user"@"localhost";
mysql> FLUSH PRIVILEGES;
mysql> quit;
```

### Clone project from GitHub into virtual environment

```sh
$ virtualenv studentsdb
$ cd studentsdb
$ source bin/activate
(studentsdb)$ mkdir src
(studentsdb)$ cd src
(studentsdb)$ mkdir media
(studentsdb)$ git clone https://github.com/PyDev777/studentsdb.git
```

### Requirements [[ list ](requirements.txt)]

```sh
(studentsdb)$ cd studentsdb
(studentsdb)$ pip install -r requirements.txt
```

### Create settings files with your values from [dev](studentsdb/dev_settings_template.py)&[prod](studentsdb/prod_settings_template.py) templates

```sh
(studentsdb)$ cd studentsdb
(studentsdb)$ cp dev_settings_template.py dev_settings.py
(studentsdb)$ cp prod_settings_template.py prod_settings.py
```

### Migrate and superuser create

```sh
(studentsdb)$ cd ..
(studentsdb)$ ./manage.py makemigrations
(studentsdb)$ ./manage.py migrate
(studentsdb)$ ./manage.py createsuperuser
```

### Run

```sh
(studentsdb)$ ./manage.py runserver
```
Visit to http://localhost:8000/ in your browser




# Source

### [Vitaliy Podoba](http://www.vitaliypodoba.com/) with practical web development [course](http://www.vitaliypodoba.com/books/django-for-beginners/) with Python/Django




# Author

### :copyright: 2017, [Dmytro Koltsuk]
