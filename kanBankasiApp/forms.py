from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput


class RegistrationForm(UserCreationForm):
	il_sec=Il.objects.all()
	ilce_sec = Ilce.objects.all()
	kanGrubu_sec = KanGrubu.objects.all()
	BOOL_CHOICES = ((True, 'Erkek'), (False, 'Kadın'))
	ad = forms.CharField(max_length=30, required=False)
	soyad = forms.CharField(max_length=30, required=False)
	email = forms.EmailField(max_length=254)
	cinsiyet = forms.TypedChoiceField(choices=BOOL_CHOICES, widget=forms.RadioSelect(attrs=dict(required=True)),coerce=bool)
	dogum_tarihi = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1950, 2000)))
	il = forms.ModelChoiceField(queryset=il_sec, widget=forms.Select(attrs=dict(required=True,placeholder='İl')))
	ilce = forms.ModelChoiceField(queryset=ilce_sec, widget=forms.Select(attrs=dict(required=True,placeholder='İlçe')))
	telefon = forms.CharField(max_length =11 ,widget=forms.TextInput(attrs=dict(required=True,placeholder='Telefon')))
	kanGrubu = forms.ModelChoiceField(queryset=kanGrubu_sec, widget=forms.Select(attrs=dict(required=True,placeholder='Kan Grubu')))

	class Meta:
		model = User
		fields = ('username','password1','password2','email','ad', 'soyad', 'cinsiyet', 'dogum_tarihi', 'il','ilce' ,'kanGrubu')

class HastaneKayitForm(forms.ModelForm):
	#sifre = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = Hastane
		fields = ('hastane_adi','il','ilce','eposta','sifre')

class KurumsalGirisYapForm(forms.ModelForm):
	class Meta:
		model = Hastane
		fields = ('hastane_adi','il','ilce','eposta','sifre')
		widgets = {
            "hastane_adi": HiddenInput(),
            "il": HiddenInput(),
            "ilce": HiddenInput(),
        }


