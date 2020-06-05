from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
#from django.forms.fields import DateField
from django import forms


class CalenderForm(forms.Form):
    date = forms.DateField(widget=AdminDateWidget(
        attrs={'placeholder': 'dd/mm/yyyy'}))


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "login__inner--text", "placeholder": "Password"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': "login__inner--text", "placeholder": "Username"}))
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "login__inner--text", "placeholder": "First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "login__inner--text", "placeholder": "Last Name"}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': "login__inner--text", "placeholder": "Email ID"}))

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']


class EngineerForm(forms.Form):
    comments = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'value': 'enter'}))
    status = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'value': 'enter'}))


class task(forms.Form):

    task = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dropdown__text', 'placeholder': 'Enter TASK'}))
