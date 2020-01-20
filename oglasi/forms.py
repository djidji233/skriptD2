from django.contrib.auth.models import User
from django import forms

from oglasi.models import Oglas


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','email','password']

class SearchForm(forms.ModelForm):
    class Meta:
        model = Oglas
        fields = ['title']