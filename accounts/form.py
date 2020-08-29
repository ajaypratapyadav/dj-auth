from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """
    Override UserCreationForm with custom user table field
    """
    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    """
    Override UserChangeForm with custom user table field
    """
    class Meta:
        model = CustomUser
        fields = '__all__'


class SignUpForm(UserCreationForm):
    """
    create signup form with custom fields to display
    Also make email field as email input
    """
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = CustomUser
        fields = '__all__'
