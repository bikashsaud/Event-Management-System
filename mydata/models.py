from django.db import models

# Create your models here.
class Programmer_detail(models.Model):
    junior='Junior'
    mid_level='Mid_level'
    senior='Senior'
    Other='Other'
    level=((junior,'Junior'),(mid_level,'Mid_level'),(senior,'Senior'),(Other,'Other'),)
    name=models.CharField(max_length=100)
    Address=models.CharField(max_length=50)
    level=models.CharField(max_length=50,choices=level,default='Junior')

    
    def __str__(self):
        return self.name
