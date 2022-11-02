from django.urls import path
from .views import *
from add.views import show_json

app_name = 'statistic'

urlpatterns = [
    path('', show_statistic, name="show_statistic"),
    path('json/', show_json, name="show_json"),
]