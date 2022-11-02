from django.urls import path
from report.views import *



app_name = 'report'

urlpatterns = [
    path('', show_report, name='show_report'),
    path('target/', show_target, name='show_target'),
    path('json/', show_json_ajax, name='show_json_ajax'),
    path('add/', add_todolist_ajax , name='add_todolist_ajax'),
    path('delete/<int:id>/', delete_todolist_ajax, name='delete_todolist_ajax'),
]