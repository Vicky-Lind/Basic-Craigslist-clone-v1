from django.urls import path, include
from . import views
from my_app import views

urlpatterns = [
    path('', views.home, name='home'),
]