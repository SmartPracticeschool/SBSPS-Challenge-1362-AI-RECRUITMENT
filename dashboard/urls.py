from django.urls import path, include
from . import views

urlpatterns = [
    path('login/',views.login, name='login'),
    path('login/',views.logout, name='logout'),
    path('', views.index, name='index')
]
