## Django Base User

### Create a django app user custom model


#### MOTIVATION
It is highly recommended, every time you create a project, to override django's default user model. See [Django’s built-in User model is not always appropriate](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#substituting-a-custom-user-model:~:text=Django%E2%80%99s%20built%2Din%20User%20model%20is%20not%20always%20appropriate)

### Requiriments
- git
- make
- python 3.11 or higher
### recomended
- pyenv and install python version of your choice

### How to use

clone this repository into empty directory
~~~shell
$ git clone https://github.com:marcospsviana/django-base-user.git
~~~
rename directory for your project name
~~~shell
$ mv django-base-user your-project-directory && cd your-project-directory
~~~
setup initial the app user for project and install principal dependencies 
~~~shell
$ make setup
~~~
Setup will make venv by name .venv and install dependencies, after remove remote git repository 

activate your environment 

~~~shell
$ source .venv/bin/activate
~~~
Create you project django
~~~shell
$ django-admin startproject your-project-name .
~~~
If you want, after creating the project, you can move the app user directory into the project directory
~~~shell
mv users your-project-name/
~~~
Apply migrations user
~~~shell
$ python manage.py makemigrations
~~~
The output maybe like this:
~~~shell
Migrations for 'users':
  yourproject-name/users/migrations/0001_initial.py
    - Create model User 
~~~

Migrate
~~~shell
$ python manage.py migrate
~~~
Output: 
~~~shell
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, users
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0001_initial... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying users.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying sessions.0001_initial... OK
~~~


#### Use make for format code whith blue and check with flake8 

check code with flake8
~~~shell
$ make check
~~~
sorted imports with isort and format code with blue
~~~shell
$ make format
~~~

Enjoy
