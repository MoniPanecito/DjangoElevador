from django.db import models

# Create your models here.
class Project(models.Model):
    sensor1 = models.CharField(max_length=10, null=True)
    sensor2 = models.CharField(max_length=10, null=True)
    sensor3 = models.CharField(max_length=10, null=True)