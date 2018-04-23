from django.db import models
from django.contrib.auth.models import User


class Il(models.Model):
	il_adi = models.CharField(max_length = 30)

	def __str__(self):
		return self.il_adi






