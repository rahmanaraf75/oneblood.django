from django.shortcuts import render,redirect
from accounts.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'accounts.html')


def registerview(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account is created for ' + user)
            return redirect('log in')
    else:
        form = RegisterForm()
    context = {'form': form}
    return render(request, 'register.html',context)

def loginview(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'login.html', context)

def logoutview(request):
    logout(request)
    return redirect('log in')