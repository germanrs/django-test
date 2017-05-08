# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from laptop.forms import LaptopForm
from laptop.models import Laptop

# Create your views here.
def index(request):
	return render(request, 'laptop/index.html')

def laptop_view(request):
	if request.method == 'POST':
		form = LaptopForm(request.POST)
		if form.is_valid():
			form.save()
		#return redirect('laptop:index')
		return redirect('laptop:laptop_listar')
	else:
		form = LaptopForm()

	return render(request, 'laptop/laptop_formulario.html', {'form':form})

def laptop_list(request):
	laptop = Laptop.objects.all()
	contexto = {'laptop':laptop}
	return render(request, 'laptop/laptop_listar.html', contexto)

def laptop_edit(request, laptop_id):
	laptop = Laptop.objects.get(id=laptop_id)
	if request.method == 'GET':
		form = LaptopForm(instance=laptop)
	else:
		form = LaptopForm(request.POST, instance=laptop)
		if form.is_valid():
			form.save()
		return redirect('laptop:laptop_listar')
	return render(request, 'laptop/laptop_formulario.html', {'form':form})

def laptop_delete(request, laptop_id):
	laptop = Laptop.objects.get(id=laptop_id)
	if request.method == 'POST':
		laptop.delete()
		return redirect('laptop:laptop_listar')
	return render(request, 'laptop/laptop_borrar.html', {'laptop':laptop})

class LaptopList(ListView):
	model = Laptop
	template_name = 'laptop/laptop_listar.html'

class LaptopCreate(CreateView):
	model = Laptop
	form_class = LaptopForm
	template_name = 'laptop/laptop_formulario.html'
	success_url = reverse_lazy('laptop:laptop_listar')

class LaptopUpdate(UpdateView):
	model = Laptop
	form_class = LaptopForm
	template_name = 'laptop/laptop_formulario.html'
	success_url = reverse_lazy('laptop:laptop_listar')

class LaptopDelete(DeleteView):
	model = Laptop
	template_name = 'laptop/laptop_borrar.html'
	success_url = reverse_lazy('laptop:laptop_listar')