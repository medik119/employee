from django import form 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    model = User
    fields = ('first_name','last_name','email')

