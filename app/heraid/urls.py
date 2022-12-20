from django.urls import path

from .views import HomeView, ResourceInformationView

# app_name = "heraid"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("types-of-abuse/", ResourceInformationView.as_view(), name="types-of-abuse"),
]
