from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
# Create your views here.
class datalist(View):
    def create_datalist(self,request):
        return HttpResponse('Data List views is here')
