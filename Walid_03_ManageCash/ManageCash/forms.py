from django import forms
from ManageCash.models import *
from django.contrib.auth.forms import UserCreationForm


class userForm(UserCreationForm):
    class Meta:
        model = customUser
        fields = ['username', 'email', 'password1', 'password2']


class profileForm(forms.ModelForm):
    class Meta:
        model = customUser
        fields = ['username', 'email']


class addCashForm(forms.ModelForm):
    class Meta:
        model = AddCash
        fields = '__all__'
        exclude = ['user', 'datetime']

        widgets = {
            'datetime' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            )
        }

class expenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        exclude = ['user', 'datetime']

        widgets = {
            'datetime' : forms.DateInput(
                attrs={
                    'type' : 'date'
                }
            )
        }