# Chapter 2 - Book Shop - Project Setup
 
![Image](1.PNG)

![Image](2.PNG)

![Image](3.PNG)

![Image](4.PNG)

![Image](5.PNG)

![Image](6.PNG)

![Image](7.PNG)

![Image](8.PNG)

![Image](9.PNG)

![Image](10.PNG)

![Image](11.PNG)

# Project Setup Commands

```
pip install django
```

```
django-admin startproject config .
```

```
python manage.py startapp backend 
```

```
config -> settings.py
```

# Application definition

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'backend'
]
```