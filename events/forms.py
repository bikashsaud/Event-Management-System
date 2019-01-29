from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model

from Account.models import UserProfile
from create_event.models import Create_Event
from get_token.models import Get_Token

class CreateForm(forms.ModelForm):
    class Meta:
        model=Create_Event
        exclude=['user']
        # fields='__all__'
class GetTokenForm(forms.ModelForm):
    class Meta:
        model=Get_Token
        exclude=['user','event']


#for sending email test
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = UserProfile
        fields = ('email', 'name','password1', 'password2')
