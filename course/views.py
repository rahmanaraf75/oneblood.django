from django.shortcuts import render,redirect
from course.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request,'course.html')


def registerview(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
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
            return redirect('course')

    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return render(request)