from django.shortcuts import render
from django.views import generic
from kanBankasiApp.models import *
from kanBankasiApp.forms import *



class HomePageView(generic.ListView):
	template_name="home.html"

	def get_queryset(self):
		return "helo"

class RegistrationView(generic.FormView):
	form_class = RegistrationForm
	template_name = "signup.html"
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class HastaneKayit(generic.FormView):
	form_class = HastaneKayitForm
	template_name = "hastaneKayit.html"
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)
	
class HakkımızdaView(generic.ListView):
	template_name="hakkımızda.html"

<<<<<<< HEAD
	def get_queryset(self):
		return "hello"
=======
class KurumsalGirisYap(generic.FormView):
	form_class = KurumsalGirisYapForm
	template_name = "kurumsalGiris.html"
	success_url = '/'
>>>>>>> 5785fbde48a001c7d6b9b686c51eed5de2ab9a32
