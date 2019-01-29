from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from .import views
from django.conf.urls.static import static

urlpatterns=[
url(r'^create-event/',views.create,name='create_event'),
url(r'event-detail/(?P<id>[0-9]+)/$',views.event_detail,name='event_detail'),
url(r'^get-token/(?P<id>[0-9]+)/$',views.get_token,name='get_token'),
url(r'^send_mail/$',views.send_mail,name='send_mail'),
url(r'^dashboard/',views.dashboard,name='dashboard'),
url(r'^delete-event/(?P<id>[0-9]+)/$',views.delete_event,name='delete'),
url(r'^cancle-event/(?P<id>[0-9]+)/$',views.cancle_event,name='cancle'),
]
