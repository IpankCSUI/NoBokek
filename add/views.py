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

@csrf_exempt
def add_income(request):
    if request.method == 'POST':
        income = request.POST.get('income')
        desc_in = request.POST.get('desc_in')
        date = datetime.date.today()
        user = request.user
        money_obj = Money.objects.create(income=income, desc_in = desc_in, date=date, user=user)

        result = {
            'fields':{
                'income':money_obj.income,
                'desc_in':money_obj.desc_in,
                'date':money_obj.date,
            },
            'pk':money_obj.pk
        }
        return JsonResponse(result)

@csrf_exempt
def add_outcome(request):
    if request.method == 'POST':
        outcome = request.POST.get('outcome')
        desc_out = request.POST.get('desc_out')
        date = datetime.date.today()
        user = request.user
        money_obj = Money.objects.create(outcome=outcome, desc_out = desc_out, date=date, user=user)
        
        result = {
            'fields':{
                'outcome':money_obj.outcome,
                'desc_out':money_obj.desc_out,
                'date':money_obj.date,
            },
            'pk':money_obj.pk
        }
        return JsonResponse(result)