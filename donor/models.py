from django.db import models
from django.contrib.auth.models import User
from userprofile.models import profile

# Create your models here.
class Donor(models.Model):
    d_id = models.TextField(max_length=20, primary_key=True)
    profile_no = models.ForeignKey(profile, null=True, on_delete=models.CASCADE)
    d_availablity = models.CharField(max_length=5)
    d_last_donation_date = models.FloatField(max_length=10)

class receiver(models.Model):
    rec_id = models.TextField(max_length=20, primary_key=True)
    profile_no = models.ForeignKey(profile, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    rec_contact = models.IntegerField(max_length=15)