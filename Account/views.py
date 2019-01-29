from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from django.http import HttpResponse
from .forms import UserCreationForm,UserLoginForm

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import UserProfile

# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
User=get_user_model()



def register(request,*args,**kwargs):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render(request,'register.html',{'form':form})

def login_(request,*args,**kwargs):
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        new_user=User.objects.get(email__iexact=form.cleaned_data.get('email'))
        login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
        return redirect("index")
    return render(request,"login.html",{'form':form})


def logout_(request):
    logout(request)
    return redirect('login')
