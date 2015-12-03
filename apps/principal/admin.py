from django.contrib import admin
from .models import Articulo, Inventario, Almacen, Cliente,Vendedor

class ArticuloAdmin(admin.ModelAdmin):
	list_display = ('id','nombre','precio','caducidad')
	list_filter = ('nombre',)

class InvetarioAdmin(admin.ModelAdmin):
	list_display = ('id','articulo','existencia','almacen')
	list_filter = ('articulo',)


class AlmacenAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre','virtual')
	list_filter = ('nombre',)

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'calle', 'numero', 'celular','telefono','municipio')
	list_filter = ('nombre', 'celular')

class VendedorAdmin(admin.ModelAdmin):
	list_display = ('id', 'nombre', 'celular','colonia','direccion')
	list_filter = ('nombre','celular')

admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Inventario, InvetarioAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Vendedor,VendedorAdmin)
