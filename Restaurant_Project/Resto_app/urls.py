from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
]