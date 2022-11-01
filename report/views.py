# from django.shortcuts import render
# from django.core import serializers
# from django.http import HttpResponseRedirect
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
# from django.http.response import JsonResponse
# from .models import Pesan, ReportUser
# import json

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
from django.http.response import JsonResponse
import json
# def show_report(request):
#     data_barang_wishlist = ReportUser.objects.all()
#     context = {
#     'list_barang': data_barang_wishlist,
#     'nama': 'Kak Cinoy'
#     }
#     return render(request, "report.html")


def show_report(request):
    transactionUser = ReportUser.objects.all()
    response = {
        'transactionUser': transactionUser,
        
    }
    return render(request, 'report.html', response)

def pesan(request):
    # username = 'anon'
    if request.user.is_authenticated:
        username = request.user
        print(username)

    if request.POST:
        nama = username
        isi = request.POST.get('isi')
        Pesan.objects.create(nama=nama, isi=isi)
        return HttpResponseRedirect('/report')
        
    else:
        form = FormPesan()
        Pesans = Pesan.objects.all()

        for Pesan in Pesans:
            print(Pesan)
        
        context = {
            'Pesans':Pesans,
            'form':form
        }
        return render(request, 'report.html', context)

def pesanajax(request):
    argument = request.GET['q']
    username = request.user
    Pesan.objects.create(nama=username, isi=argument)
    datastr = serializers.serialize("json", Pesan.objects.filter(nama=request.user))
    data = json.loads(datastr)

    return JsonResponse(data, safe=False)