from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('handleCounter', views.handleCounter, name='handleCounter'),
    path('login', views.login, name='login'),
    path('handleRegister', views.handleRegister, name='handleRegister'),

    path('reg', views.reg, name='reg'),
    path('logout', views.logout, name='logout'),
    path('posts', views.posts, name='posts'),
    path('post_details/<int:id>', views.post_details, name='post_details'),
    path('users', views.list_users, name='users'),
    path('weather', views.weather, name='weather'),

]
