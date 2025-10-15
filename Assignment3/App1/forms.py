from django import forms
from .models import Employee

class Empform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        
        
        widgets = {
            'Date_of_joining': forms.DateInput(
                attrs= {'class':'form-control','type':'date'}
            ),
        }
        