from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Customer

class RegistrationForm(UserCreationForm):
    
       fields = (first_name, last_name, email, password, )
