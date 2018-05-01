from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from kanBankasiApp.views import *

urlpatterns = [
	url(r'^$', HomePageView.as_view()),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
]
