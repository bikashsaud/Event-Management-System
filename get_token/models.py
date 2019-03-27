from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import datetime
from django.utils import timezone
from datetime import date

from Account.models import UserProfile
from create_event.models import Create_Event

class Get_Token(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    event=models.ForeignKey(Create_Event,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    Email=models.EmailField(max_length=150,unique=True)
    # Address=models.CharField(max_length=150)
    Male="male"
    Female="Female"
    Sex=((Male,'male'),(Female,'Female'))
    Gender=models.CharField(max_length=150,choices=Sex,default='Male')
    Age=models.IntegerField(default=0)
    Cell_Phone=models.IntegerField()
    def __str__(self):
        return self.Email
