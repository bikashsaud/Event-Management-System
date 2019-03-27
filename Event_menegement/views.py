from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .import views
from slider.models import Slider
from create_event.models import Create_Event
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import(
            CreateView,
            DetailView,
            ListView,
            UpdateView,
            DeleteView
)
class index(ListView):
    template_name='index.html'
    model=Create_Event
    context_object_name='form'
    def get_queryset(self):
        form1=Create_Event.objects.all()
        return form1
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['slider']=Slider.objects.all()[:1]
        return context
