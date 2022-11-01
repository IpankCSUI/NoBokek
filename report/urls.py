from django.urls import path
from report.views import show_report,pesanajax



app_name = 'report'

urlpatterns = [
    path('', show_report, name='show_report'),
    path('pesanajax/', pesanajax, name='pesanajax'),
    
]