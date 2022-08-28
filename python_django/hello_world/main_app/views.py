from django.http import HttpRequest
from django.http.response import HttpResponse

def homeView(request):
    return HttpResponse("Hello There! This is my first progect in Django framework. It seems disgusting till now. Hope for the enjoyable something as go forward.")
