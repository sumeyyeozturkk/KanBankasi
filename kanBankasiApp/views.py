from django.shortcuts import render
from django.views import generic
from kanBankasiApp.models import *
from kanBankasiApp.forms import *



class HomePageView(generic.ListView):
	template_name="index.html"

	def get_queryset(self):
		return "helo"

class RegistrationView(generic.FormView):
	form_class = RegistrationForm
	template_name = "signup.html"
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

