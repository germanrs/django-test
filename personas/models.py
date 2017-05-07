# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from laptop.models import Laptop

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=30)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=10)
	email= models.EmailField()
	laptop = models.ForeignKey(Laptop, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre