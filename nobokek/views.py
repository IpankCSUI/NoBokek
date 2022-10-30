from django.shortcuts import render
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
from nobokek.models import BarangWishlist
from nobokek.forms import Stat
from nobokek.models import ContactUs
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime 
...
...
@login_required(login_url='/nobokek/login/')
def show_nobokek(request):
    data_keluhan = ContactUs.objects.all()
    context = {
        'list_keluhan': data_keluhan,      
    }
    return render(request, "nobokek.html", context)

def show_guest(request):
    data_barang_wishlist = BarangWishlist.objects.all()
    context = {
        'list_barang': data_barang_wishlist,
        'nama': 'Kak Cinoy',
        
    }
    return render(request, "guest.html", context)

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("nobokek:show_nobokek")) # membuat response
            response.set_cookie('last_login', str(datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
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

def show_statistic(request: HttpRequest):
    if request.method == "POST":
        form = Stat(request.POST)
        if form.is_valid():
            task = BarangWishlist(
                date=str(datetime.datetime.now().date()),
                harga_barang=form.cleaned_data["harga"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Saved success!")
            return redirect("nobokek:show_nobokek")
    form = Stat()
    context = {"form": form}
    return render(request, "", context)

@login_required(login_url="/nobokek/login")
def create_task(request):
    if request.method == "POST":
        name = request.POST.get('nama')
        email = request.POST.get('alamat')
        problem = request.POST.get('masalah')

        new_task = ContactUs(user=request.user, nama=name, alamat=email, masalah=problem, date=datetime.now())
        new_task.save()
        return redirect("nobokek:show_nobokek")
    return render(request, "contact.html")

@login_required(login_url="/nobokek/login")
def show_nobokek_json(request):
    tasks = ContactUs.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', tasks), content_type='application/json')

def add_task(request):
    if request.method == "POST":
        name = request.POST.get('nama')
        email = request.POST.get('alamat')
        problem = request.POST.get('masalah')

        new_task = ContactUs(user=request.user, nama=name, alamat=email, masalah=problem, date=datetime.now())
        new_task.save()
    return HttpResponse('')