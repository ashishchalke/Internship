from django import forms
from . models import Leave_Quota

class Leave_Quotaform(forms.ModelForm):
    class Meta:
        model = Leave_Quota
        fields = "__all__"