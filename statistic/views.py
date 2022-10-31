from django.shortcuts import HttpResponse, render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.core import serializers
from django.contrib import messages

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

def show_something(request: HttpRequest):
    if request.method == "POST":
        form = (request.POST)
        if form.is_valid():
            task = Stat(
                date=str(datetime.datetime.now().date()),
                income=form.cleaned_data["income"],
                outcome=form.cleaned_data["outcome"],
                user=request.user,
            )
            task.save()
            messages.success(request, "Saved success!")
            return redirect("nobokek:show_nobokek")
    form = Stat()
    context = {"form": form}
    return render(request, "", context)