from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("FMAS/<str:token>", views.index, name="index"),
    path("FMAS/sheSayYes/<str:token>", views.accept, name="accept")
]
