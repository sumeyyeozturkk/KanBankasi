from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	il_sec=Il.objects.all().values()
	ilce_sec = Ilce.objects.all().values()
	BOOL_CHOICES = ((True, 'Erkek'), (False, 'Kadın'))
	
	ad = forms.CharField(max_length=30, required=False, help_text='Optional.')
	soyad = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	cinsiyet = forms.TypedChoiceField(choices=BOOL_CHOICES, widget=forms.RadioSelect(attrs=dict(required=True)),coerce=bool)
	dogum_tarihi = forms.DateField(label='Date of birth', widget=forms.SelectDateWidget(years=range(1950, 2000)))
	il = forms.ChoiceField(choices=il_sec, widget=forms.Select(attrs=dict(required=True,placeholder='Il')))
	ilce = forms.ChoiceField(choices=ilce_sec, widget=forms.Select(attrs=dict(required=True,placeholder='Ilce')))
	telefon = forms.CharField(max_length =11 ,widget=forms.TextInput(attrs=dict(required=True,placeholder='telefon')))
	
	class Meta:
		model = User
		fields = ('username','password1', 'password2', 'email','ad', 'soyad', 'cinsiyet', 'dogum_tarihi', 'il','ilce' )