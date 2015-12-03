from django.db import models
from apps.principal.models import TimeStampModel
# Create your models here.

class Venta(TimeStampModel):

	op2 = (
			('Semana', 'Semana'),
			('Quincena', 'Quincena'),
			('Mes', 'Mes'),
		)

	cliente = models.ForeignKey('principal.Cliente')
	inventario = models.ForeignKey('principal.Inventario')
	cantidad = models.IntegerField(default=0, null=True, blank=True)
	enganche = models.DecimalField(max_digits=8, decimal_places=2)
	fechaventa  = models.DateField(null=True, blank=True)
	vendedor  = models.ForeignKey('principal.Vendedor')
	apartir = models.DateField()
	abono = models.DecimalField(max_digits=8, decimal_places=2,null=True, blank=True)
	observacion = models.TextField() 
	tipocobro = models.CharField(max_length=10, choices=op2, default='Semana')

	def __unicode__(self):
		return self.cliente.nombre


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
		return self.venta.cliente.nombre
 

