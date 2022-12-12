from unicodedata import name
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.urls import reverse
import json
from .models import PendapatForum
from .forms import AddPendapatForum
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



def add_pendapat_forum(request):
    form = AddPendapatForum()
    forum = PendapatForum.objects.all().order_by('-id').distinct()
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = AddPendapatForum(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message' : 'success'})
    nameList = PendapatForum.objects.all()
    return render(request, 'AddPendapatForum.html',{'form': form, 'forum':forum, 'nameList':nameList})

def show_forum(request):
    forum = PendapatForum.objects.all().order_by('-id').distinct()
    nameList = PendapatForum.objects.all()
    return render(request,'guest_forum.html',{'forum':forum,'nameList':nameList})

def show_json_ajax(request):
    pendapat = PendapatForum.objects.all()
    return HttpResponse(serializers.serialize('json', pendapat), content_type='application/json')

def button(request):
    return render(request, 'buttons.html',{})

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def search_pendapat_forum(request):
    form = AddPendapatForum()
    target = request.GET.get('search_box')
    forum_filter = PendapatForum.objects.filter(nama__icontains = target).order_by('-id')
    if is_ajax(request):
        form = AddPendapatForum(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message':'success'})
    if request.user.is_authenticated:
        return render(request,'AddPendapatForum.html',{'form' : form,'forum':forum_filter})
    else:
        return render(request,'guest_forum.html',{'form' : form,'forum':forum_filter})

def get_data(request):
    nameList = PendapatForum.objects.all().values
    return JsonResponse({'object': nameList})

@csrf_exempt
def add_data_pendapat_forum(request):
        nama = request.POST.get('nama')
        jurusan = request.POST.get('jurusan')
        angkatan = request.POST.get('angkatan')
        pendapat = request.POST.get('pendapat')
        data = PendapatForum(
            nama = nama, 
            jurusan = jurusan, 
            angkatan = angkatan, 
            pendapat = pendapat,
        )
        data.save()
        return JsonResponse({'target':'new target'})

