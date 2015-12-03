from django import forms
from .models import Articulo, Almacen, Inventario, Cliente, Vendedor

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = Articulo
		exclude = ['user']
                
        nombre= forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de cliente','size': '70'}))
        #fechaventa = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),  input_formats=['%d/%m/%Y'])	

        caducidad = forms.DateField(('%d/%m/%Y',),
                widget=forms.DateInput(format='%d/%m/%Y', attrs={
                'placeholder':'fecha caducidad',
                'class':'datePicker', 
                'size':'15'
                })
                )
 


class AlmacenForm(forms.ModelForm):
	class Meta:
		model = Almacen
		exclude = ['user']
        nombre = forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de Almacen ','size': '70'}))
        

class MovInvForm(forms.ModelForm):
        class Meta:
                model = Inventario
                exclude = ['user']

class ReciboForm(forms.ModelForm):
	class Meta:
		model = Inventario
		exclude = ['user']


class ClienteForm(forms.ModelForm):
	class Meta:
		model = Cliente
		exclude = ['user']


        nombre= forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de cliente','size': '70'}))
        celular = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Celular','size':'10'}))
        telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Telefono','size':'10'}))
        colonia = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Colonia','size':'70'}))
        calle = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Calle','size':'70'}))
        numero = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'placeholder':'Numero','size':'8'}))
        lado = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Lado','size':'70'}))
        frentre = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Frente','size':'60'}))
        #casa = forms.CharField(max_length=8,widget=forms.TextInput(attrs={'placeholder':'Casa','size':'8'}))
        fachada = forms.CharField(max_length=80,widget=forms.TextInput(attrs={'placeholder':'Fachada','size':'60'}))
        entre = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Entre','size':'60'}))
        municipio = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Municipio','size':'60'}))
        #longitud = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Longitud','size':'10'}))
        #latitud = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Longitud','size':'10'}))
        #estado =  forms.CharField(max_length=25,widget=forms.TextInput(attrs={'placeholder':'Estado','size':'25'})) 


class VendedorForm(forms.ModelForm):
        class Meta:
                model = Vendedor
                exclude = ['user']


        nombre= forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de Vendedor','size': '70'}))
        colonia = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'colonia','size':'70'}))
        direccion = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Direccion','size':'70'}))
        celular = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Celular','size':'10'}))
        telefono = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'placeholder':'Telefono','size':'10'}))
        estado= forms.CharField(max_length=180,widget=forms.TextInput(attrs={'placeholder':'Nombre de Estado','size': '70'}))
        municipio = forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder':'Municipio','size':'70'}))


