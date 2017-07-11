from django.db import models
from apps.principal.models import TimeStampModel
# Create your models here.

class Venta(TimeStampModel):

	opcob = (
			('Semana', 'Semana'),
			('Quincena', 'Quincena'),
			('Mes', 'Mes'),
		)

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

	inventario = models.ForeignKey('principal.Inventario')
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	enganche = models.DecimalField(max_digits=8, decimal_places=2)
	fechaventa  = models.DateField(null=True, blank=True)
	vendedor  = models.ForeignKey('principal.Vendedor')
	apartir = models.DateField()
	abono = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	observacion = models.TextField() 
	tipocobro = models.CharField(max_length=10, choices=opcob, default='Semana')

	def __unicode__(self):
		return self.nombre


	def monto(self):
		return self.inventario.articulo.precio*self.cantidad


class Cxc(TimeStampModel):
	tipo  = models.IntegerField() # 100 venta -- 200 abonos
	venta = models.ForeignKey('Venta') 
	total = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	abono = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
	proxcobro = models.DateField(null=True, blank=True)
	fechaabono = models.DateField(null=True, blank=True)
	saldo = models.DecimalField(max_digits=8, decimal_places=2,null=True,blank=True)
	pagado = models.BooleanField(default=False)
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return self.venta.nombre
 

