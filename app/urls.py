from django.urls import path
from django import views
from . import views
urlpatterns = [   
    path('', views.index, name="index"),
    path('listar', views.list, name="list"),
    path('delete', views.delete, name="delete"),
    path('add', views.add, name="add"),
    path('update', views.update, name="update"),
]   