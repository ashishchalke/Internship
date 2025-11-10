from django.db import models

# Create your models here.
leave = [
    ('sick leave','sick leave'),
    ('casual leave','casual leave'),
    ('PL','PL'),
    ('LWP','LWP')
]

class Leave_Quota(models.Model):
    quotaid = models.AutoField(primary_key=True)
    employeeid = models.ForeignKey('App1.Employeemodel',on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=100,choices=leave)
    total_quota = models.IntegerField()
    used_quota = models.IntegerField()
    remain_quota = models.IntegerField()