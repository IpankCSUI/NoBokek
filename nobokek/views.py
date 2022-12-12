import json
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from nobokek.forms import ContactForm
from nobokek.models import ContactUs
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

def show_guest(request):
    return render(request, "guest.html")

@login_required(login_url='/nobokek/login/')
def show_nobokek(request):  
    return render(request, "nobokek.html")

@login_required(login_url='/nobokek/login/')
def show_problem(request):
    data_problem = ContactUs.objects.filter(user=request.user)
    form = ContactUs()
    context = {
    'list_problem' : data_problem,
    'form' : form
    }
    return render(request, "contact.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('nobokek:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_flutter(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def flutter_register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        is_user_already_exist = User.objects.filter(username=username).exists();
        if not is_user_already_exist:
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return JsonResponse({
                "status": True,
                "username": user.username,
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Failed to register, username already exist."
            }, status=401)
    else:
        return JsonResponse({
            "status": "error"
        }, status=401)

@csrf_exempt
def logout_flutter(request):
    try:
        logout(request)
        return JsonResponse({
            "status": True,
            "message": "Successfully Logged out!"
        }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("nobokek:show_nobokek")) # membuat response
            # response.set_cookie('last_login', str(datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('nobokek:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/nobokek/login/')
def show_json(request):
    problem = ContactUs.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', problem), content_type='application/json')

def create_problem(request):
    nama = request.POST.get('nama')
    alamat = request.POST.get('alamat')
    masalah = request.POST.get('masalah')
    create_problem_ajax = ContactUs(
        user = request.user,
        nama = nama,
        alamat = alamat,
        masalah = masalah,
    )
    create_problem_ajax.save()
    return JsonResponse({"contactus": "new contactus"})

def add_todolist_ajax(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    add_todolist_ajax = ContactUs(
        user = request.user,
        title = title,
        description = description,
    )
    add_todolist_ajax.save()
    return JsonResponse({"target": "new target"})