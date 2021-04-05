from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text=_('Required. Provide a valid email address for account confirmation.'))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
