from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.acc),
    path("log",views.login),
    path('sig',views.signup),
]