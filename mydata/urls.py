from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from mydata.views import datalist
from django.views.generic import TemplateView
# from events.views import EventDetail
from django.conf.urls.static import static

urlpatterns=[
url(r'^datalist_create/',TemplateView.as_view(template_name="datalist.html")),
]
