from django.urls import path
from report.views import show_report


app_name = 'report'

urlpatterns = [
    path('', show_report, name='show_report'),
    
]