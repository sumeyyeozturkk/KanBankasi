from django.shortcuts import render
from django.views import generic
from kanBankasiApp.models import *
from kanBankasiApp.forms import *
from django.http import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# def edit_profile(request):
#     if request.method == 'POST':
#         form = ProfilForm(request.POST, instance=request.user)

#         if form.is_valid():
#             form.save()
#             return redirect(reverse('hakkimizda'))
#     else:
#         form = ProfilForm(instance=request.user)
#         args = {'form': form}
#         return render(request, 'kullaniciProfil.html', args)

def user_profile(request):
	# if request.method == 'GET':
	# 	if not Kullanici.objects.filter(user=request.user.id):
	# 		Kullanici.objects.create(user=request.user)
	if request.method == 'POST':
		form = ProfilForm(request.POST,instance=request.user.profile)
		if form.is_valid():
			user = request.user
			kullanici = Kullanici.objects.filter(user=request.user.id)
			kullanici.update(
			user = user,
			ad = form.cleaned_data['ad'],
			soyad = form.cleaned_data['soyad'],
			cinsiyet = form.cleaned_data['cinsiyet'],
			dogum_tarihi = form.cleaned_data['dogum_tarihi'],
			il = form.cleaned_data['il'],
			ilce = form.cleaned_data['ilce'],
			kanGrubu = form.cleaned_data['kanGrubu']
			)
			return HttpResponseRedirect('/hakkimizda')
		else:
			form = ProfilForm(instance=request.user.profile)
	form = ProfilForm()
	return render(request,'kullaniciProfil.html',{'form': form})



class HomePageView(generic.ListView):
	template_name="home.html"

	def get_queryset(self):
		return "helo"

class KayitOlView(generic.FormView):
	form_class = UserForm
	template_name = "signup.html"
	success_url = '/login'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class DuyuruYapView(generic.FormView):
	form_class = DuyuruForm
	template_name = "duyuruYap.html"
	success_url = '/duyurular'

	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

class DuyuruListView(LoginRequiredMixin,generic.ListView):
	template_name = "duyurular.html"
	def get_queryset(self):
		return Duyuru.objects.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["duyurulist"] = Duyuru.objects.all()
		return context

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

class HakkımızdaView2(generic.ListView):
	template_name="hakkımızda2.html"

	def get_queryset(self):
		return "hello"
# class KurumsalGirisYap(generic.FormView):
# 	form_class = KurumsalGirisYapForm
# 	template_name = "kurumsalGiris.html"
# 	success_url = '/'


# class DuyurularView(generic.ListView):
#     template_name="duyurular.html"

#     def get_queryset(self):
#         return "hello"


def giris(request):
    form = KurumsalGirisYapForm
    if(request.method=='POST'):
        giris_kontrol = KurumsalGirisYapForm(data=request.POST)
        if(giris_kontrol.is_valid()):
        	eposta = form.cleaned_data['eposta'],
        	sifre = form.cleaned_data['sifre'],
        return HttpResponseRedirect('/hakkimizda')
    return render(request,'kurumsalGiris.html',locals())
