from django.db import models

# Create your models here.
Leave_type = [
    ('SL','SL'),
    ('CL','CL'),
    ('PL','PL'),
    ('LWP','LWP')
]


Status = [
    ('approved','approved'),
    ('rejected','rejected'),
    ('pending','pending'),
]
class Managermodel(models.Model):
    Manager_id = models.AutoField(primary_key=True)
    Manager_name = models.CharField(max_length=100)
    
class Employeemodel(models.Model):
    Emp_id = models.AutoField(primary_key=True)
    Emp_name = models.CharField(max_length=100)
    Manager = models.ForeignKey('Managermodel',on_delete=models.CASCADE,related_name='leaves_applied')
    
    
class Leavemodel(models.Model):
    leaveid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('Employeemodel',on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100,choices=Leave_type)
    reason = models.CharField(max_length=200,default='Leave reason')
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    total_days = models.IntegerField()
    status = models.CharField(max_length=200,choices=Status)
    approved_by = models.ForeignKey('Employeemodel',on_delete=models.SET_NULL,related_name='leave_approved',null=True)

