from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .import views
from slider.models import Slider
from create_event.models import Create_Event
from django.core.mail import send_mail, BadHeaderError


def index(request):
    form=Create_Event.objects.all()
    slide={'slider':Slider.objects.all()[:1],'form':form}
    # start of mail
    #send_mail(subject,message,from_email,to_list,fail_silently=True)
    # example is below
    # send_mail('EVENT CREATED MESSAGE ','Message For you ','saudbikash514@yahoo.com',['saudbikash514@gmail.com'],fail_silently=False)
    # end of send mail
    return render(request,'index.html',slide)
