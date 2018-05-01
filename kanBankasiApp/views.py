from django.shortcuts import render
from django.views import generic


class HomePageView(generic.ListView):
	template_name="index.html"

	def get_queryset(self):
		return "helo"
