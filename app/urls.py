from django.urls import path
from django import views
from . import views
urlpatterns = [   
    path('', views.index, name="index"),
    path('list', views.list, name="list"),
    path('delete', views.delete, name="delete"),
    path('add', views.add, name="add"),
    path('update', views.update, name="update"),
    #path planes de estudio
    path('listplan', views.listplan, name="listplan"),
    path('listp', views.listp, name="listp"),


]   