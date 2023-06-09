from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from captcha.fields import CaptchaField

User = get_user_model()

class SignUpForm(UserCreationForm):
    # добавьте дополнительные поля, такие как имя, фамилия, электронная почта и т.д.
    capthca = CaptchaField()
    class Meta:
        model = User
        fields = ('email', 'password')

class Loginform(forms.Form):
    email = forms.CharField(max_length= 25,label="Enter email")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

