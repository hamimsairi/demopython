from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='penganjur_home'),
    path('aktiviti/add/', views.penganjur_new, name='penganjur_add'),
]