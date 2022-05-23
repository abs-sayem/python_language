from django.urls import path
from . import views     # Here, dot(.) means current directory. Whenever we want to iprt something from same directory, we'll use dot(.)

urlpatterns = [
    path('', views.homeView, name='home')       # This will appear in the page.
]