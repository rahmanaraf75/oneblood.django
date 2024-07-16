from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    profile_no= models.TextField(max_length=20, primary_key=True)
    user= models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    blood_group= models.CharField(max_length=10)
    medical_report= models.TextField(max_length=100)
    address=models.CharField(max_length=25)
    contact=models.IntegerField()
