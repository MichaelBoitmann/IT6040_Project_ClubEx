from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text="Required, enter valid email address")

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'subscription' )
