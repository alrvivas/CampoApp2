# encoding:utf-8
from django import forms
from .models import *

class direccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
