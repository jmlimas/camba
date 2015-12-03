from django.contrib import admin
from .models import Venta, Cxc
from apps.principal.models import Articulo

class VentaAdmin(admin.ModelAdmin):
	list_display = ('id','cliente','inventario','fechaventa','tipocobro')
	list_filter = ('id','cliente',)
 

class CxcAdmin(admin.ModelAdmin):
	list_display = ('id', 'venta','get_fechaventa','total', 'abono', 'fechaabono','pagado','saldo','tipo','status')


	#def get_articulo(self, obj):
	#	return obj.venta.articulo.nombre
	#get_articulo.admin_order_field='articulo'
	#get_articulo.short_descripcion = 'articulo'


	def get_fechaventa(self, obj):
		return obj.venta.fechaventa
	get_fechaventa.admin_order_field = 'fechaventa'
	get_fechaventa.admin_order_field = 'fechaventa'


admin.site.register(Venta, VentaAdmin)
admin.site.register(Cxc, CxcAdmin)

 