from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('', views.index, name = 'homepage'),
    path('new/', views.index, name = 'new'),
    path('hot/', views.hot, name = 'hot'),
    path('tag/<str:tagid>', views.tag, name='tag'),
    path('question/<int:id>', views.question, name='question'),
    path('login/', views.login, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('ask/', views.ask, name = 'ask')
]