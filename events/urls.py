from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from .import views

from events.views import Dashboard,Create_Events,event_detail
from django.conf.urls.static import static

# from django.views.generic import TemplateView

urlpatterns=[
url(r'^create-event/$',Create_Events.as_view(),name='create_event'),
url(r'event-detail/(?P<pk>[0-9]+)/$',event_detail.as_view(),name='event_detail'),
url(r'^get-token/(?P<id>[0-9]+)/$',views.get_token,name='get_token'),
url(r'^send_mail/$',views.send_mail,name='send_mail'),
url(r'^dashboard/(?P<pk>[0-9]+)/$',Dashboard.as_view(),name='dashboard'),
url(r'^delete-event/(?P<id>[0-9]+)/delete/$',views.Delete_Event.as_view(),name='delete'),
url(r'^cancle-event/(?P<id>[0-9]+)/$',views.cancle_event,name='cancle'),
]
