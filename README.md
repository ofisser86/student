Students Attendance Tracking Service

GitHub license Coverage


This service tracking the attendance of your students via web    :busts_in_silhouette: :eyes:


Functional

Available functions depends by rights of visitor:

Anonimous rights

site language selection
social login (automatically register as User after login)
register on site (becomes User after email confirmation)
view all students in one list
bidirectional ordering of students on columns
User rights

site language selection
standard/social login
CRUD students/groups
enroll students into groups
specify group leader
mark attendance of students in journal
filtering students by selected group
bidirectional ordering of students/groups on columns
edit his profile
reset/change his password
Spec User rights (permission is added by Administrator)

all User rights
view actions log
send letter to Administrator
Administrator rights

overlord has all rights
Technical Stack

Ubuntu 14.04, Python 2.7.6, MySQL 14.14 Distrib 5.5.47
Git 1.9.1, PIP 1.5.4, Virtualenv 1.11.4,
Django 1.7.11, Twitter Bootstrap 3.3.6, jQuery 1.11.3
Features

Development and Production modes

Bootstrap Responsive Web Design allows working on any device
English/Ukrainian language selection on site (I18N/L10N)
Access to functionality, based on the visitors rights
2-step customized user registration on site with Registration Redux
Standard and Social (Facebook) login, reset/change password support
User profile use User model extended by additional fields
AJAX mode for all requests on site (page reload is absent)
Browser History for AJAX mode with navigation in AJAX mode
All forms are Bootstrap Modal and Crispy Forms
Captcha in login, registration, password reset and send letter forms
Remember selected language and selected group in cookies
Pagination and bidirectional ordering of all lists by columns
Use widget for input date in User profile and Student profile
Custom widget for view photo in User profile and Student profile
Customized logging system for write specified events to .log file
Custom signals for logging actions and tracking errors by email
Customized Admin interface for user profile additional fields
Customized Admin interface for students search, filter, edit, validation
Custom context processors for origin and groups variables
Custom tag pagenav display page navigation for only given list of objects
Custom filter str2int convert input string into integer. If impossible return 0
Custom filter nice_username return user full name if exist, else username.
Additionally, wrapping by * for staff, by ** for superuser
Development mode only

Custom middleware DBTimeMiddleware display DB queries count and time
Custom middleware RequestTimeMiddleware display request time
Custom commands stcount prints number of specified objects in a DB
Custom commands filldb creates specified number (1..10) of objects in DB
Custom commands localize_static set static to online/offline usage mode
Installation

Dependencies

$ sudo apt-get install python-dev libxml2-dev libxslt-dev libfreetype6-dev libjpeg8-dev zlib1g-dev
PIP, Virtualenv and Git (if not installed)

$ sudo apt-get install pip==1.5.4 virtualenv==1.11.4 git==1.9.1
MySQL (if not installed)

$ sudo apt-get install mysql-server mysql-client libmysqlclient-dev
$ sudo mysql_install_db
$ sudo /usr/bin/mysql_secure_installation
Create DB and DB-User

$ mysql -u root -p
mysql> CREATE DATABASE students_db CHARACTER SET utf8 COLLATE utf8_general_ci;
mysql> CREATE USER "students_db_user"@"localhost" IDENTIFIED BY "password";
mysql> GRANT ALL PRIVILEGES ON students_db.* TO "students_db_user"@"localhost";
mysql> FLUSH PRIVILEGES;
mysql> quit;
Clone project from GitHub into virtual environment

$ virtualenv studentsdb
$ cd studentsdb
$ source bin/activate
(studentsdb)$ mkdir src
(studentsdb)$ cd src
(studentsdb)$ mkdir media
(studentsdb)$ git clone https://github.com/PyDev777/studentsdb.git
Requirements [ list ]

(studentsdb)$ cd studentsdb
(studentsdb)$ pip install -r requirements.txt
Create settings files with your values from dev&prod templates

(studentsdb)$ cd studentsdb
(studentsdb)$ cp dev_settings_template.py dev_settings.py
(studentsdb)$ cp prod_settings_template.py prod_settings.py
Migrate and superuser create

(studentsdb)$ cd ..
(studentsdb)$ ./manage.py makemigrations
(studentsdb)$ ./manage.py migrate
(studentsdb)$ ./manage.py createsuperuser
Run

(studentsdb)$ ./manage.py runserver
Visit to http://localhost:8000/ in your browser

Tests

(studentsdb)$ ./manage.py test
(studentsdb)$ ./manage.py test_coverage
Mentor

Vitaliy Podoba with practical web development course with Python/Django

My gratitude to mentor

I am deeply grateful to my teacher for this wonderful course and practical
experience of web development, obtained and applied by me for create this project.
I wish him success and prosperity!
Author

:copyright: 2016, Dmytro K
