# Taken from: https://github.com/irinatu17/Art-of-Tea
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
]
