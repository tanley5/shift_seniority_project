from django import forms
from django.forms import fields

from .models import Shift


class ShiftUpdateForm(forms.ModelForm):
    class Meta:
        model = Shift
        fields = ['report_name', 'datetime_created', 'shift']
