from asyncio.windows_events import NULL
from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import datetime

from django.contrib.auth.decorators import login_required
@login_required(login_url='/nobokek/login/')
def show_add(request):
    data_money = Money.objects.filter(user=request.user)
    form = AddIncomeOutcome()
    context = {
    'list_money' : data_money,
    'form' : form
    }
    return render(request, "add.html", context)

@login_required(login_url='/nobokek/login/')
def show_json(request):
    money = Money.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', money), content_type='application/json')

@login_required(login_url='/nobokek/login/')
@csrf_exempt
def add_income(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        desc_in = request.POST.get('desc_in')
        # desc_out =NULL
        # outcome=NULL
        date = datetime.date.today()
        user = request.user
        money_obj = Money.objects.create(income=income, desc_in = desc_in, date=date, user=user)
        # money_obj = Money.objects.create(user=user, income=income, outcome=outcome, desc_in=desc_in, desc_out=desc_out,date=date)

        result = {
            'fields':{
                'income':money_obj.income,
                # 'outcome':NULL,
                'desc_in':money_obj.desc_in,
                # 'desc_out':NULL,
                'date':money_obj.date,
            },
            'pk':money_obj.pk
        }
        return JsonResponse(result)

# @csrf_exempt
# def add_outcome(request):
#     if request.method == 'POST':
#         outcome = request.POST.get('outcome')
#         desc_out = request.POST.get('desc_out')
#         date = datetime.date.today()
#         user = request.user
#         money_obj = Money.objects.create(user=user, income = NULL, outcome=outcome, desc_in = NULL, desc_out = desc_out, date = date)
        
#         result = {
#             'fields':{
#                 'outcome':money_obj.outcome,
#                 'desc_out':money_obj.desc_out,
#                 'date':money_obj.date,
#             },
#             'pk':money_obj.pk
#         }
#         return JsonResponse(result)

@login_required(login_url='/nobokek/login/')
@csrf_exempt
def add_outcome(request):
    if request.method == 'POST':
        # income = NULL
        outcome = request.POST.get('outcome')
        desc_out = request.POST.get('desc_out')
        # desc_in = NULL
        date = datetime.date.today()
        user = request.user
        money_obj = Money.objects.create(outcome=outcome, desc_out = desc_out, date=date, user=user)
        # money_obj = Money.objects.create(user=user, income=income, outcome=outcome, desc_in=desc_in, desc_out=desc_out,date=date)

        result = {
            'fields':{
                # 'income':NULL,
                'outcome':money_obj.outcome,
                # 'desc_in':NULL,
                'desc_out':money_obj.desc_out,
                'date':money_obj.date,
            },
            'pk':money_obj.pk
        }
        return JsonResponse(result)

@login_required(login_url='/nobokek/login/')
@csrf_exempt
def add_note(request):
    if request.method == 'POST':
        user = request.user
        note = request.POST.get('note')
        new_note = Money.objects.create(user=user, note=note)

        result = {
            'fields':{
                'note':new_note.note,
            },
            'pk':new_note.pk
        }
        return JsonResponse(result)

@login_required(login_url='/login/')
@csrf_exempt
def delete_note(request, id):
    if (request.method == 'DELETE'):
        Money.objects.filter(id=id).delete()
        return HttpResponse(status=202)