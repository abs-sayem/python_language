> To create a templete in Django--
    > follow the previous steps of -
        > create a project
        > include the project name in settings,py file
        > create a urls.py file into main_app directory
        > In the urls file import 'from . import views'     # Here, dot(.) means current directory
        > and add the path of 'HomeView' class from 'view.py'
    > frist 'rom django.views.generic import TemplateView'
    > create a class and include 'index.html' file   # working with class than function is more dynamic
    > create a template directory into main_app and a 'index.html' file into it.