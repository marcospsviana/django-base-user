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
$ git clone https://github.com:marcospsviana/django-base-user
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