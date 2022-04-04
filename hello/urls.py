from django.urls import path

from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("moon", views.moon, name="moon")
]