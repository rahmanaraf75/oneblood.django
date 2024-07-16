from django.shortcuts import render, redirect
from blood_request.forms import BloodRequestForm
# Create your views here.
def bloodrequest_view(request):
    form = BloodRequestForm()
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render (request,'blood_request.html')