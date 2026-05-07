# Django

create a Django project 
```bash
django-admin startproject myproject
```

create a Django app
```bash
cd myproject
python manage.py startapp blog
```

add the app to settings.py
```python
# myproject/myproject/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Add your app here
]
```

add the app's urls to the project urls
```python
# myproject/myproject/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
```

create a urls.py file in the blog app
```python
# myproject/blog/urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog_home, name='blog_home'),
]
```

create a view in the blog app
```python
# myproject/blog/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def blog_home(request):
    # return HttpResponse("Welcome to the Blog Home Page!")
    template = loader.get_template('first-blog.html')
    return HttpResponse(template.render({}, request))
```

create a template for the blog home page
```html
<!-- myproject/blog/templates/first-blog.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Home</title>
</head>
<body>
    <h1>Welcome to the Blog Home Page!</h1>
</body>
</html>
```

run the development server

```bash
python manage.py runserver

```

