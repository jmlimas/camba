from django import forms
from .models import Venta, Cxc

class VentaForm(forms.ModelForm):
		class Meta:
			model = Venta
			exclude = ['user']

		cliente_display = forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de alumno','size': '60'}))
		observacion = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Comentarios' ,'rows':'3', 'cols': '60'}))
		cantidad = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'cantidad'}))
		enganche = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'enganche'}))
		abono    = forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'abono'}))
       
		fechaventa = forms.DateField(('%d/%m/%Y',),
		widget=forms.DateInput(format='%d/%m/%Y', attrs={
		'placeholder':'fecha venta',
		'class':'datePicker', 
		'size':'10'
		})
		)

		apartir = forms.DateField(('%d/%m/%Y',),
		widget=forms.DateInput(format='%d/%m/%Y', attrs={
		'placeholder':'Fecha de Cobra apartir ',
		'class':'datePicker', 
		'size':'15'
		})
		)



		def __init__(self, *args, **kwargs):
			super(VentaForm, self).__init__(*args, **kwargs)
			self.fields['cliente_display'].label = "Cliente"
			self.fields['cliente'].widget = forms.HiddenInput() # apago el  combo del cliente para que no se vea. :)




class CobroForm(forms.Form):
	abono = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'abono','size':'16'}))
	
	proxcobro = forms.DateField(('%d/%m/%Y',),
		widget=forms.DateInput(format='%d/%m/%Y', attrs={
		'placeholder':'fecha proximo Cobro',
		'class':'datePicker', 
		'size':'15'
		})
		)
	
	class Meta:
		model = Cxc
		exclude = ['user']

