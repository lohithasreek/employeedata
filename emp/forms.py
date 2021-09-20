from django import forms
from .models import Empl


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Empl
        fields="__all__"

