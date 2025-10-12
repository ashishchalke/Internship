from django import forms
from .models import Formsmodel

class Formsform(forms.ModelForm):
    class Meta:
        model = Formsmodel
        fields = "__all__"