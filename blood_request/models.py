from django.db import models
from donor.models import Donor

# Create your models here.

class Blood_request(models.Model):
    req_id = models.TextField(max_length=20, primary_key=True)
    blood_group = models.CharField(max_length=10)
    blood_amount = models.TextField(max_length=10)
    patient_name = models.CharField(max_length=20)
    request_purpose = models.CharField(max_length=50)
    request_address = models.TextField(max_length=15)
    special_notes = models.CharField(max_length=50)

class Blood_receieved(models.Model):
    brec_id = models.TextField(max_length=20, primary_key=True)
    req_id = models.ForeignKey(Blood_request, null=True, on_delete=models.CASCADE)
    d_id = models.ForeignKey(Donor, null=True, on_delete=models.CASCADE)
    rec_id = models.TextField(max_length=20)
    datetime =models.CharField(max_length=20)
