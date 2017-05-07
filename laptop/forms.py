from django import forms

from laptop.models import Laptop

class LaptopForm(forms.ModelForm):

	class Meta:
		model = Laptop

		fields = [
			'serie',
			'uuid',
			'modelo',
		]
		labels = {
			'serie' : 'Serie XO',
			'uuid' : 'UUID XO',
			'modelo': 'Modelo XO',
		}
		widgets = {
			'serie' : forms.TextInput(attrs={'class':'form-control'}),
			'uuid' : forms.TextInput(attrs={'class':'form-control'}),
			'modelo': forms.Select(attrs={'class':'form-control'}),
		}
