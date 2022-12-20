from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"


class ResourceInformationView(TemplateView):
    template_name = "types-of-abuse.html"
