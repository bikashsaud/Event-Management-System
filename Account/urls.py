from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, login_, logout_

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login_,name='login'),
    url(r'^logout/$',views.logout_,name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
