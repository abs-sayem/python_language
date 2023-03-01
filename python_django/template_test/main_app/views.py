from django.views.generic import TemplateView

class HomeView(TemplateView):
    # template_name is a variable situated in TemplateView. We basically overwrite the variable and place 'index.html' to it.
    template_name = "index.html"
    