from django.shortcuts import HttpResponse, render, redirect
from django.http import HttpRequest
from django.core import serializers

from add.models import Money
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='/nobokek/login/')
def show_statistic(request):
    data_user = Money.objects.filter(user=request.user)
    context = {
    'list_data' : data_user,
    }
    return render(request, "statistic.html", context)

