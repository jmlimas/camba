from django.db import models
from django.conf import settings

class TimeStampModel(models.Model):
	user     = models.ForeignKey(settings.AUTH_USER_MODEL,db_index=True)
	fecha    = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True) 

	class Meta:
		abstract = True


class Articulo(TimeStampModel):
	nombre = models.CharField(max_length=150)
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	caducidad = models.DateField()

	def __unicode__(self):
		return self.nombre

class Almacen(TimeStampModel):
	nombre = models.CharField(max_length=140)
	virtual = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nombre

class Inventario(TimeStampModel):
	articulo = models.ForeignKey('Articulo')
	existencia = models.IntegerField(default=0)
	almacen = models.ForeignKey('Almacen')

	def __unicode__(self):
		return self.articulo.nombre

	def preciototal(self):
		return self.articulo.precio*self.existencia





class Cliente(TimeStampModel):
	op = (
			('1 piso', '1 piso'),
			('2 pisos', '2 pisos'),
		)

	op2 = (
			('Vigente', 'Vigente'),
			('Cancelado', 'cancelado'),
			('incobrabrle','incobrabrle'),
		)

	nombre = models.CharField(max_length=180)
	celular = models.CharField(max_length=10, null=True, blank=True)
	telefono = models.CharField(max_length=10, null=True, blank=True)
	colonia = models.CharField(max_length=120)
	calle = models.CharField(max_length=120)
	numero = models.CharField(max_length=8)
	lado = models.CharField(max_length=80)
	frentre = models.CharField(max_length=80)
	casa = models.CharField(max_length=8, choices=op)
	fachada = models.CharField(max_length=80)
	entre = models.CharField(max_length=120)
	municipio = models.CharField(max_length=120)
	lon = models.FloatField(null=True, blank=True,default=1.63789)
	lat = models.FloatField(null=True, blank=True,default=-77.7452081)
	estado = models.CharField(max_length=25, choices=op2, default='Vigente',null=True, blank=True)


	def __unicode__(self):
		return self.nombre


class Vendedor(TimeStampModel):
	nombre = models.CharField(max_length=250)
	direccion = models.CharField(max_length=180)
	colonia = models.CharField(max_length=150)
	celular = models.CharField(max_length=10)
	telefono  = models.CharField(max_length=10)
	estado    = models.CharField(max_length=80)
	municipio = models.CharField(max_length=80)
	estatus   = models.BooleanField(default=True)


	def __unicode__(self):
		return self.nombre





