from django.urls import path
from . import views     # Since, views and urls are in the same directory. Here dot(.) means current directory

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),    # 'as_view()' is defined in HomeView
]