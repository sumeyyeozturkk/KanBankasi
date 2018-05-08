from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from kanBankasiApp.views import *
from kanBankasiApp import views

urlpatterns = [
	url(r'^$', HomePageView.as_view(),name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$',RegistrationView.as_view(),name='signup'),
    url(r'^hastane/$', HastaneKayit.as_view(),name ='hastane'),
	url(r'^hakkimizda/$',HakkımızdaView.as_view(),name='hakkimizda'),
    url(r'^kurumsalgiris/$', KurumsalGirisYap.as_view(),name='kurumsalgiris'),
    url(r'^kullaniciProfil/$', views.edit_profile, name = 'kullaniciProfil'),
	url(r'^duyurular/$',DuyurularView.as_view(),name='duyurular'),


]
