from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
class HomeView(TemplateView):
    template_name = "home.html"
class SignView(TemplateView):
    template_name = "signin.html"
class ConfView(TemplateView):
    template_name = "conf.html"
class re_login(TemplateView):
    template_name = "re_login.html"