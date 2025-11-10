from django import forms
from . models import Managermodel,Leavemodel,Employeemodel


class Managerform(forms.ModelForm):
    class Meta:
        model = Managermodel
        fields = "__all__"
        
        
class Leaveform(forms.ModelForm):
    class Meta:
        model = Leavemodel
        fields = "__all__"
        
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employeemodel
        fields = "__all__"