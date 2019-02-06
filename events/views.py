from django.shortcuts import render,redirect

from django.utils import timezone
from datetime import date

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout

from django.db.models import Q
from django.http import FileResponse
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from Account.models import UserProfile
from .forms import CreateForm,SignupForm,GetTokenForm
from create_event.models import Create_Event
from get_token.models import Get_Token
#
# Create your views here

def create(request):
    if request.user.is_authenticated():

        form=CreateForm(request.POST or None,request.FILES)
        form1=UserProfile.objects.get(id=request.user.id)
        context={
            'form':form,
        }
        if form.is_valid():
            data=form.save(commit=False)
            data.user_id=form1.id
            data.save()
            # start of mail
            #send_mail(subject,message,from_email,to_list,fail_silently=True)
            # example is below

            send_mail('EVENT CREATED MESSAGE '
            ,'Thank you for creating Event in our system donot forget us anothe',
            'saudbikash514@yahoo.com',
            ['saudbikash514@gmail.com'],
            fail_silently=False)
            # end of send mail
            return redirect('index')
        return render(request,'create_event.html',context)
    else:
        return redirect('login')
def event_detail(request,id):
    if request.user.is_authenticated():
        form=Create_Event.objects.filter(id=id)
        context={"form":form,}
        return render(request,"detail.html",context)
    else:
        return redirect('login')

# def send_email(request):
#     subject = request.POST.get('subject', '')
#     message = request.POST.get('message', '')
#     from_email = request.POST.get('from_email', '')
#     if subject and message and from_email:
#         try:
#             send_mail(subject, message, from_email, ['admin@example.com'])
#         except BadHeaderError:
#             return HttpResponse('Invalid header found.')
#         return HttpResponseRedirect('/contact/thanks/')
#     else:
#         # In reality we'd use a form class
#         # to get proper validation errors.
#         return HttpResponse('Make sure all fields are entered and valid.')
def get_token(request,id):
    if request.user.is_authenticated():
        form=GetTokenForm(request.POST or None)
        ins1=Create_Event.objects.filter(id=id)
        ins2=UserProfile.objects.get(id=request.user.id)
        context={"form":form,"ins1":ins1,"ins2":ins2,}
        if form.is_valid():
            profile=form.save(commit=False)
            profile.user_id=ins2.id
            profile.event_id=id
            profile.save()
            send_mail('EVENT Registered MESSAGE For you','WelCome!! your Registration is successfully Accepted## Thanks for Register !!!@','saudbikash514@yahoo.com',['saudbikash514@gmail.com'],fail_silently=False)
            return redirect('index')
        else:
            return render(request,'get_token.html',context)
    else:
        return redirect('login')

#  for paticular user_id
def dashboard(request):
    if request.user.is_authenticated():
        form1=UserProfile.objects.get(id=request.user.id)
        form2=Create_Event.objects.filter(user_id=request.user.id)
        form3=Get_Token.objects.filter(user_id=request.user.id)
        context={"form1":form1,"form2":form2,"form3":form3,}
        return render(request,"dashboard.html",context)
    else:
        return redirect('index')

# Delete Event BY who create event_title
def delete_event(request,id):
    if request.user.is_authenticated():
        try:
            doct=Create_Event.objects.get(id=id)
            doct.delete()
            return redirect('dashboard')
        except:
            return redirect('index')
    else:
        return redirect('login')

#cancle event br who register Event
def cancle_event(request,id):
    if request.user.is_authenticated():
        try:
            doct=Get_Token.objects.get(id=id)
            doct.delete()
            return redirect('dashboard')
        except:
            return redirect('index')
    else:
        return redirect('login')


def contact(request):
    """Send Contact Email"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            send_mail_from = 'noreply@khophi.co'
            # this sender refers to person who the email is from
            # as indicated in the contact form
            recipients = ['contact@khophi.co', form.cleaned_data['sender']]

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/help/contact?sent=yes')  # Redirect after POST
    else:
        form = ContactForm()  # An unbound form
    return render(request, 'contact.html', {'form': form, 'sent': request.GET.get('sent', '') })
