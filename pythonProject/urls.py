"""pythonProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import accounts.views as accounts
import home.views as home
import userprofile.views as userprofile
import donor.views as donor
import find_donor.views as findDonor
import blood_request.views as bloodrequest
import contact.views as contact
import about.views as about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home.home, name='home'),
    path('userprofile/',userprofile.userprofile_view, name='profile'),
    path('donor/',donor.donor_view, name='donor'),
    path('find_donor/',findDonor.findDonor_view, name='find donor'),
    path('blood_request/',bloodrequest.bloodrequest_view, name='blood request'),
    path('about/',about.about_view, name= 'about'),
    path('contact/', contact.contact_view, name='contact'),
    path('register/', accounts.registerview, name='be a donor'),
    path('', accounts.loginview, name='log in'),
    path('logout/', accounts.logoutview, name='log out'),
]
