from django import forms
from . models import Review,Employee

class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        
    
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"