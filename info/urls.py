from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='info'),
    path('how_to_buy/', views.how_to_buy, name='how_to_buy'),
]
