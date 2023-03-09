from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('handleCounter', views.handleCounter, name='handleCounter'),
    path('login', views.login, name='login'),
    path('handleRegister', views.handleRegister, name='handleRegister'),
]
