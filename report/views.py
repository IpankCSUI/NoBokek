from django.shortcuts import render
import datetime
from django.urls import reverse
from django.core import serializers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from add.models import Money
from report.models import Target

@login_required(login_url='/nobokek/login/')
def show_report(request):
    transactionUser = Money.objects.all()
    response = {
        'transactionUser': transactionUser,
        'userName': request.user,
        
    }
    return render(request, 'report.html', response)

@login_required(login_url='/nobokek/login/')
def get_username(request):
    username = request.user,
    return HttpResponse(serializers.serialize('json', username), content_type='application/json')

@login_required(login_url='/nobokek/login/')
def show_target(request):
    targetUser = Target.objects.filter(user=request.user)
    response = {
        'targetUser': targetUser,
        'userName': request.user,
        
    }
    return render(request, 'target.html', response)

@login_required(login_url='/nobokek/login/')
def show_json_ajax(request):
    targetuser = Target.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', targetuser), content_type='application/json')

@login_required(login_url='/nobokek/login/')
@csrf_exempt
def add_todolist_ajax(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    add_todolist_ajax = Target(
        user = request.user,
        title = title,
        description = description,
    )
    add_todolist_ajax.save()
    return JsonResponse({"target": "new target"})

@login_required(login_url='/nobokek/login/')
@csrf_exempt
def delete_todolist_ajax(request,id):
    target = Target.objects.filter(pk=id)   
    target.delete()
    return JsonResponse({"target": "clear target"})


