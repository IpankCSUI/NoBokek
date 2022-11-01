from django.shortcuts import HttpResponse, render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.core import serializers

import datetime
from statistic.models import Stat

# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='/nobokek/login/')
def show_statistic(request: HttpRequest):
    data_money = Stat.objects.filter(user=request.user)
    context = {
    'list_data' : data_money,
    }
    return render(request, "statistic.html", context)

@login_required(login_url='/nobokek/login/')
def show_json(request):
    money = Stat.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', money), content_type='application/json')
