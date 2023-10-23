# auth_app/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')
