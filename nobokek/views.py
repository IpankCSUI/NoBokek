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
    form = ContactForm()
    if request.method == 'POST':
        nama = request.POST.get('nama')
        alamat = request.POST.get('alamat')
        masalah = request.POST.get('masalah')
        date = datetime.date.today()
        user = request.user
        problem_obj = ContactUs.objects.create(nama=nama, alamat=alamat, masalah=masalah, date=date, user=user)
        result = {
            'fields':{
                'nama':problem_obj.nama,
                'alamat':problem_obj.alamat,
                'masalah':problem_obj.masalah,
                'date':problem_obj.date,
                'user':problem_obj.user.username,
            },
            'pk':problem_obj.pk
        }
        return JsonResponse(result)
    return render(request, 'contact.html', {'form': form})

