from django.db import models

# Create your models here.
class courseDetails(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    syllabus = models.TextField()