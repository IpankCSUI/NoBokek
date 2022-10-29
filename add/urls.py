from audioop import add
from django.urls import path, include
from .views import *

app_name = 'add'

urlpatterns = [
    path('', show_add, name = "show_add"),
    path('json/',show_json,name="show_json"),
    path('addincome/', add_income, name='add_income'),
    path('addoutcome/', add_outcome, name='add_outcome')
]