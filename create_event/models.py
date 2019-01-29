from django.db import models
from Account.models import UserProfile
from ckeditor.fields import RichTextField
from django.utils.timezone import datetime
from django.utils import timezone
from datetime import date
# Create your models here.


class Create_Event(models.Model):
    Education='Education'
    Fashion='Fashion'
    Food='Food'
    Other='Other'
    Fair='Fair'
    Conference='Conference'
    Party='Party'

    category=((Education,'Education'),(Fashion,'Fashion'),(Food,'Food'),(Other,'Other'), )
    types=((Fair,'Fair'),(Conference,'Conference'),(Party,'Party'),(Other,'Other'), )
    
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    event_title=models.CharField(max_length=150)
    category=models.CharField(max_length=50,choices=category,default='Category')
    type=models.CharField(max_length=50,choices=types,default='Types')
    organizer=models.CharField(max_length=150)
    Location=models.CharField(max_length=150)
    start_date=models.DateField(default=timezone.now())
    end_date=models.DateField(default=timezone.now())
    start_time=models.TimeField(default='12:00')
    end_time=models.TimeField(default='12:00')
    image=models.ImageField(upload_to='events/',blank=True,null=True)
    description=RichTextField(default=0)

    def __str__(self):
        return self.event_title
