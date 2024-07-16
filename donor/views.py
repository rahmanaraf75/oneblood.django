from django.shortcuts import render

# Create your views here.
def donor_view(request):
    return render (request,'donor.html')