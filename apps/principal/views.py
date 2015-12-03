from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView, UpdateView
from .models import Articulo,Almacen,Inventario, Cliente, Vendedor
from apps.venta.models import Venta
from .forms import ArticuloForm, AlmacenForm, ReciboForm, ClienteForm, VendedorForm, MovInvForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from datetime import date 
from django.db.models import Q
from django.db.models import Sum
from django.http import JsonResponse

from django.shortcuts import redirect
from django.db.models import F

# Create your views here.
 

class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView,self).get_context_data(**kwargs)
		today = date.today()
		context['vtahoy'] = Venta.objects.filter(fechaventa__year=today.year,
		fechaventa__month=today.month,fechaventa__day=today.day).count()
		context['artvta'] = Venta.objects.values('inventario__articulo__nombre').annotate(total = Count('cantidad'))
		context['vendor'] = Venta.objects.values('vendedor__nombre').annotate(total = Count('vendedor'))
		context['stockruta'] = Inventario.objects.filter(almacen__virtual='True').aggregate(Sum('existencia')).values()[0]  
		context['stock'] = Inventario.objects.aggregate(Sum('existencia')).values()[0]
		context['invaloruta'] = Inventario.objects.aggregate(total=Sum(F('existencia') * F('articulo__precio'))).values()[0]		 
		context['ultimasvtas'] = Venta.objects.all().order_by('-fecha')[:7]
		return context

	
class AddArticulo(CreateView):
	form_class = ArticuloForm
	model = Articulo
	template_name = 'articulo_form.html'
	success_url  = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddArticulo,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddArticulo, self).form_invalid(form)


class UpdateArticulo(UpdateView):
	template_name = 'articulo_form.html'
	form_class = ArticuloForm
	model = Articulo
	success_url = reverse_lazy('principal_app:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateArticulo, self).form_valid(form)

class ListArticulos(ListView):
	context_object_name = 'articulos'
	template_name = 'list_articulo.html'
	model = Articulo
	paginate_by  = 7
	success_url = '/'



class AddVendedor(CreateView):
	form_class = VendedorForm
	model = Vendedor
	template_name = 'vendedor_form.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddVendedor,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddVendedor, self).form_invalid(form)

class ListVendedor(ListView):
	context_object_name = 'venedores'
	template_name = 'list_vendedor.html'
	model = Vendedor
	paginate_by  = 7
	success_url = '/'
 

class UpdateVendedor(UpdateView):
	template_name = 'vendedor_form.html'
	form_class = VendedorForm
	model = Vendedor
	success_url = reverse_lazy('principal_app:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateVendedor, self).form_valid(form)


class AddAlmacen(CreateView):
	form_class = AlmacenForm
	model = Almacen
	template_name = 'ubicacion_form.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddAlmacen,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddAlmacen, self).form_invalid(form)

class ListAlmacen(ListView):
	context_object_name = 'almacenes'
	template_name = 'list_ubicacion.html'
	model = Almacen
	success_url = '/'

class UpdateAlmacen(UpdateView):
	template_name = 'ubicacion_form.html'
	form_class = AlmacenForm
	model = Almacen
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateAlmacen, self).form_valid(form)


class MovInv(CreateView):
	form_class = MovInvForm
	model = Inventario 
	template_name = 'movinv_form.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(MovInv,self).form_valid(form)

	def form_invalid(self, form):
		return super(MovInv, self).form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(MovInv,self).get_context_data(**kwargs)
		context['articulos'] = Articulo.objects.all()  
		return context







class AddRecibo(CreateView):
	form_class = ReciboForm
	model = Inventario
	template_name = 'recibo_form.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddRecibo,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddRecibo, self).form_invalid(form)



class ListInv(ListView):
	context_object_name = 'inve'
	template_name = 'list_iventario.html'
	model = Inventario
	paginate_by  = 7
	success_url = '/' 


	def get_context_data(self, **kwargs):
		context = super(ListInv,self).get_context_data(**kwargs)
		context['stock'] = Inventario.objects.aggregate(Sum('existencia')).values()[0]  
		#context['tt'] = Inventario.objects.aggregate(Sum('preciototal')).values()[0]
		context['total'] = Inventario.objects.aggregate(total=Sum(F('existencia') * F('articulo__precio'))).values()[0]
		return context

class ListInvMov(ListView):
	context_object_name = 'inve'
	template_name = 'list_invmto.html'
	model = Inventario
	paginate_by  = 7
	success_url = '/' 


	def get_context_data(self, **kwargs):
		context = super(ListInvMov,self).get_context_data(**kwargs)
		context['stock'] = Inventario.objects.aggregate(Sum('existencia')).values()[0]  
		#context['tt'] = Inventario.objects.aggregate(Sum('preciototal')).values()[0]
		return context



class AddCliente(CreateView):
	model = Cliente
	form_class = ClienteForm
	template_name = 'cliente_form.html'
	success_url = '/'


	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddCliente,self).form_valid(form)

	def form_invalid(self, form):
		return super(AddCliente, self).form_invalid(form)


class ListCliente(ListView):
	context_object_name = 'clientes'
	template_name = 'list_cliente.html'
	model = Cliente
	paginate_by  = 7
	success_url ='/'


class UpdateCliente(UpdateView):
	template_name = 'cliente_form.html'
	model = Cliente
	form_class = ClienteForm
	success_url = reverse_lazy('principal_app:index')

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(UpdateCliente, self).form_valid(form)


def Lista_InvAjax(request): # ajax de materias por nivel ver 1.1
	if request.is_ajax():
		mats = Inventario.objects.filter(articulo = request.GET['id_articulo'])
		secciones=[]
		for indice,elemento in enumerate(mats):
			secciones.append({
				'pk':mats[indice].pk,
				'existencia':mats[indice].existencia,
				'almacen':mats[indice].almacen.nombre, 
				}) 
		return JsonResponse(secciones, safe = False)
	else:
		return redirect('/')
