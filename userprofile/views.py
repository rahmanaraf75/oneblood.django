from django.shortcuts import render, HttpResponse

# Create your views here.
def userprofile_view(request):
    return render(request,'userprofile.html')