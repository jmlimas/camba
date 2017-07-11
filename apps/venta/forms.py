from django import forms
from .models import Venta, Cxc

class VentaForm(forms.ModelForm):
		class Meta:
			model = Venta
			exclude = ['user']

		nombre= forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de cliente','size': '70'}))
		celular = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Celular','size':'10'}))
		telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Telefono','size':'10'}))
		colonia = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Colonia','size':'70'}))
		calle = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Calle','size':'70'}))
		numero = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'placeholder':'Numero','size':'8'}))
		lado = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Lado','size':'70'}))
		frentre = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Frente','size':'60'}))
		fachada = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Fachada','size':'60'}))
		entre = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Entre','size':'60'}))
		municipio = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Municipio','size':'60'}))

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

class pronosticocxc33(forms.Form):
	fechaini = forms.DateField(('%d/%m/%Y'), 
		widget=forms.DateInput(format='%d/%m/%Y'))

	fechafin = forms.DateField(('%d/%m/%Y'), 
		widget=forms.DateInput(format='%d/%m/%Y'))
 

class pronosticocxc22(forms.Form):
    fechaini = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'fechaini', 'data-date-format':'yyyy-mm-dd'}))
    fechafin = forms.DateField(widget = forms.TextInput(attrs={'class':'form-control', 'id':'fechafin', 'data-date-format':'yyyy-mm-dd'}))
  
class pronosticocxc(forms.Form):
	fechaini = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))
	fechafin = forms.DateField(widget=forms.DateInput(attrs={'class':'datepicker'}))


