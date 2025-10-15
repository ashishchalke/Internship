from django.db import models

# Create your models here.
class Employee(models.Model):
    
    role = [
        ('Admin','Admin'),
        ('Manager','Manager'),
        ('Team Leader','Team Leader'),
        ('Employee','Employee')
    ]
    
    department = [
        ('Operation','Operation'),
        ('Sales','Sales'),
        ('Accounts','Accounts'),
        ('IT','IT')
    ]
    
    SrNo = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=255)
    Mobile_Number = models.CharField(max_length=10)
    Role = models.CharField(max_length=100,choices=role)
    Department = models.CharField(max_length=100,choices=department)
    Date_of_Joining = models.DateField(auto_now = True)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)