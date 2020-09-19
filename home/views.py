from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from .models import NewUser
from django.db.models import Q

def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('signup')
    # else:
    #     User = request.user
    context = {}
    return render(request, 'home/index.html', context)

def signup(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()

            return redirect('/home/index/')


    context = {'form': form}
    return render(request, 'home/signup.html', context)

def login(request):
    if request.method == 'GET':
        email = request.GET.get('inputEmail')
        password = request.GET.get('inputPassword')
        print(email, password)
        result = NewUser.objects.filter(Q(email=email) and Q(password=password))
        if result:
            return redirect('/home/index')

    context = {}
    return render(request, 'home/login.html', context)
