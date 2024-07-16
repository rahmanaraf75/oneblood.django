from django.shortcuts import render

# Create your views here.
def findDonor_view(request):
    return render(request,'find_donor.html')