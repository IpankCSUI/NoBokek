from django.shortcuts import render
from django.http import HttpRequest
from statistic.models import Stat
from django.contrib import messages
from django.shortcuts import redirect
import datetime

# Create your views here.
def show_statistic(request: HttpRequest):
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