from audioop import add
from django.urls import path, include
from .views import *

app_name = 'add'

urlpatterns = [
    path('', show_add, name = "show_add"),
    path('json/',show_json,name="show_json"),
    path('addincome/', add_income, name='add_income'),
    path('addoutcome/', add_outcome, name='add_outcome'),
    path('addnote/', add_note , name='add_note'),
    path('deletenote/<int:id>/', delete_note, name='delete_note'),
    path('add_income_flutter/', add_income_flutter , name='add_income_flutter'),
    path('add_outcome_flutter/', add_outcome_flutter , name='add_outcome_flutter'),
    path('add_note_flutter/', add_note_flutter , name='add_note_flutter'),
]