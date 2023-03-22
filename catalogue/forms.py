from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(forms.Form):
    ISBN = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "ISBN",
                "class": "form-control",
                "maxlength": "13",
                "minlength": "10",
            }
        ))
   