from django.shortcuts import redirect, render
from django.shortcuts import render_to_response
from models import User
from forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate


def index(request):

    if request.method == "POST":


        form = UserForm(request.POST)


        if form.is_valid():


            if form.save():

                return redirect("quests/")


    else:
        form = UserForm()
    data = {'form': form}

    return render(request, "index.html", data)


@login_required
def quests(request):
    return render_to_response('quests.html')

@login_required
def setupa(request):
    return render_to_response('setupa.html')

@login_required
def setupb(request):
    return render_to_response('setupb.html')