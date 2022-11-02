from django.urls import path
from .views import button,add_data_pendapat_forum,add_pendapat_forum,search_pendapat_forum,get_data, show_forum


urlpatterns = [
    path('',button , name='button'),
    # path('button/',button , name='button'),
    path('add_pendapat_forum/',add_pendapat_forum , name='add_pendapat_forum'),
    path('button/add_pendapat_forum/',add_pendapat_forum , name='add_pendapat_forum'),
    path('search_pendapat_forum/',search_pendapat_forum , name='search_pendapat_forum'),
    path('get_data/',get_data, name='get_data'),
    path('add_data_pendapat_forum/',add_data_pendapat_forum , name='add_data_pendapat_forum'),
    path('show_forum/',show_forum,name='show_forum'),
]