from django.urls import path
from twichtech import views

urlpatterns = [
    path("", views.home, name="home"),
]