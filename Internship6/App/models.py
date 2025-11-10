from django.db import models

# Create your models here.

class Employee(models.Model):
    Emp_Id = models.AutoField(primary_key=True)
    Emp_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Emp_name


Period = [
    ('Month', 'Month'),
    ('Quarterly', 'Quarterly'),
    ('Annually', 'Annually')
]

select_employee = [
    ('Admin', 'Admin'),
    ('Manager', 'Manager'),
    ('TL', 'TL')
]

class Review(models.Model):
    Review_Id = models.AutoField(primary_key=True)
    Review_Title = models.CharField(max_length=100)
    Select_Employee = models.CharField(max_length=100, choices=select_employee)
    Review_Date = models.DateField(auto_now_add=True)
    Employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='reviews_as_employee')
    Reviewed_by = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='reviews_as_reviewer')
    Review_Period = models.CharField(max_length=100, choices=Period)
    Enter_Rating = models.IntegerField()
    Comment = models.CharField(max_length=300, null=True, blank=True)
    Created_by = models.DateTimeField(auto_now_add=True)
    Updated_by = models.DateTimeField(auto_now=True)
    
    
    class Meta:
        db_table = 'Review'
        
        
    def __str__(self):
        return self.Review_Title