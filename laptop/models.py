# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Laptop(models.Model):
	MODELOS_XO = (
        ('1', 'XO-1'),
        ('2', 'XO-1.5'),
        ('3', 'XO-1.75'),
        ('4', 'XO-4'),
    )
	serie = models.CharField(max_length=11)
	uuid = models.CharField(max_length=32)
	modelo = models.CharField(max_length=1, choices=MODELOS_XO)

	def __unicode__(self):
		return self.serie

	def modelo_detalle(self):
		return dict(Laptop.MODELOS_XO)[self.modelo]