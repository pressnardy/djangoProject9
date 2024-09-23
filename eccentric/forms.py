from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            "username": forms.TextInput(attrs={
                'class': 'input-text',
                'id': 'username',
            }),
            "password1": forms.PasswordInput(attrs={
                'class': 'input-text',
                'id': 'password1',
            }),
            "password2": forms.PasswordInput(attrs={
                'class': 'input-text',
                'id': 'password2',
            }),
            'email': forms.EmailInput(attrs={'class': 'input-text', 'id': 'email',}),
        }


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

