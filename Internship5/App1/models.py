from django.db import models

# Create your models here.
class Taskmodel(models.Model):
    priority = [
        ('High',"High"),
        ('Medium','Medium'),
        ('Low','Low')
    ]
    
    type = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed')
    ]
    
    
    
    
    Task_id = models.AutoField(primary_key=True)
    Task_title = models.CharField(max_length=100)
    Task_description = models.CharField(max_length=300)
    Task_priority = models.CharField(max_length=200,choices=priority)
    Start_date = models.DateField(auto_now_add=True)
    End_date = models.DateField(auto_now=True)
    Task_type = models.CharField(max_length=50,choices=type)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    