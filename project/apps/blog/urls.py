from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listar/', views.post_listar, name="post_listar"),
    path('crear/', views.post_crear, name="post_crear"),
    path('about/',views.about, name="about")
]
