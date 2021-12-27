from django.urls import path
from . import views
from .dashboards import dashboard

app_name = 'dashboards'
urlpatterns = [
    path('', views.index, name='index'),
]
