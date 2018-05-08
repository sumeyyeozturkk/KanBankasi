from django.shortcuts import render
from django.views import generic
from kanBankasiApp.models import *
from kanBankasiApp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def edit_profile(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('hakkimizda'))
    else:
        form = RegistrationForm(instance=request.user)
        args = {'form': form}
        return render(request, 'kullaniciProfil.html', args)

class HomePageView(generic.ListView):
	template_name="home.html"

	def get_queryset(self):
		return "helo"

class RegistrationView(generic.FormView):
	form_class = UserForm
	template_name = "signup.html"
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)


class ProfilOlusturmaView(LoginRequiredMixin ,generic.CreateView):
	form_class = ProfilForm
	template_name ="ProfilOlusturma.html"
	success_url = '/'

	def get_form_kwargs(self):
		kwargs = super().get_form_kwargs()
		if self.request.method in ["POST"]:
			post_data = kwargs["data"].copy()
			user = self.request.user.id
			post_data["user"] = user
			kwargs["data"] = post_data
		return kwargs


class HastaneKayit(generic.FormView):
	form_class = HastaneKayitForm
	template_name = "hastaneKayit.html"
	success_url = '/'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)
	
class HakkımızdaView(generic.ListView):
	template_name="hakkımızda.html"

	def get_queryset(self):
		return "hello"

class KurumsalGirisYap(generic.FormView):
	form_class = KurumsalGirisYapForm
	template_name = "kurumsalGiris.html"
	success_url = '/'



