from django.contrib import admin
from django.urls import include, path
from . import views

app_name='zeit'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pers_nr>/', views.detail, name='detail')
]