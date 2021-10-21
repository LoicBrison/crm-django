from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from crmDjango.Back.controller import Controller
class UserForm(forms.Form):

    lastname = forms.CharField(label="Nom")
    firstname = forms.CharField(label="Prénom")
    email = forms.CharField(label="Email")
    address = forms.CharField(label="Adresse")
    phone = forms.CharField(label="Tel.")

