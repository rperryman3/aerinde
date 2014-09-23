from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from aerinde.models import List, Task

from forms import EmailUserCreationForm, ListForm, TaskForm


def index(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password1']
            user = form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("profile")
    else:
        form = EmailUserCreationForm()

    return render(request, "index.html", {'form': form})


@login_required()
def setupa(request, userid):
    if request.method == "POST":
        form = ListForm(request.POST)
        if form.is_valid():
                a = form.cleaned_data['name']
                b = userid
                new = List.objects.create(name=a, user_id=b)
                new.save()
                return redirect("setupb", b)
    else:
        form = ListForm()
    data = {'form': form}

    return render(request, 'setupa.html', data)

@login_required()
def setupb(request, userid):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
                a = form.cleaned_data['task']
                b = form.cleaned_data['deadline']
                c = form.cleaned_data['list']
                d = userid
                new = Task.objects.create(task=a, deadline=b, user_id=d)
                new.save()

                return redirect("setupb", d )
    else:
        form = TaskForm()
    data = {'form': form}

    return render(request, 'setupb.html', data)

@login_required()
def profile(request):
    return render(request, 'profile.html')

@login_required()
def quests(request):
    return render(request, 'quests.html')

@login_required()
def logout(request):
    logout(request)

