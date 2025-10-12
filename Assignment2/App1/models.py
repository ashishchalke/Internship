from django.db import models

# Create your models here.
class Formsmodel(models.Model):
    SrNo = models.CharField(max_length=20,unique=True)
    Role_Name = models.CharField(max_length=50)
    Role_Description = models.CharField(max_length=100)