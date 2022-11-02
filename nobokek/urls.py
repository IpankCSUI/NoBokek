from django.urls import path
from nobokek.views import show_nobokek
from nobokek.views import register #sesuaikan dengan nama fungsi yang dibuat
from nobokek.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from nobokek.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from nobokek.views import show_guest
from nobokek.views import show_nobokek_json, add_task, create_task

app_name = 'nobokek'

urlpatterns = [
    path('', show_nobokek, name='show_nobokek'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('guest/', show_guest, name='show_guest'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_nobokek_json, name='show_nobokek_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('add/', add_task, name="add_task"),
    path('contact/', create_task, name="contact"),
    
]