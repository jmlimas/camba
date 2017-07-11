from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView, UpdateView, FormView
from .models import Articulo,Almacen,Inventario,Vendedor
from apps.venta.models import Venta
from .forms import ArticuloForm, AlmacenForm, ReciboForm, VendedorForm, MovInvForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from datetime import date 
#from django.db.models import Q
from django.db.models import Sum
from django.http import JsonResponse,HttpResponse


from django.shortcuts import redirect,get_object_or_404
from django.db.models import F

import json
from django.views.decorators.csrf import csrf_exempt

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


class MovInv(FormView):
	form_class = MovInvForm
	model = Inventario 
	template_name = 'movinv_form.html'
	success_url = '/'

	def form_valid(self, form):
		print self.request.POST['almacen']
		 
		#inv = Inventario()

		#inv = Inventario.objects.get(pk = self.request.POST['datos'])
		#inv.existencia = inv.existencia - int(self.request.POST['existencia'])
		#inv.save() 

	
		try:
			# mueve  mercancia de  un almacen a otro.
			invmov =  Inventario.objects.get(almacen = self.request.POST['almacen'],articulo = self.request.POST['articulo'])
			invmov.existencia = invmov.existencia + int(self.request.POST['existencia'])
			invmov.save()

			# Le tumba  la  existencia  al  almacen  de  deonde  se  mueve  la  mercancia 
			inv = Inventario.objects.get(pk = self.request.POST['datos'])
			inv.existencia = inv.existencia - int(self.request.POST['existencia'])
			inv.save()
			#print 'update'
		except Inventario.DoesNotExist:
			#print 'nuevo'
			# Se  inserta  un  almacen  nuevo a la  tabla de  inventarios
			i = Inventario()
			i.user = self.request.user
			art = Articulo.objects.get(pk = self.request.POST['articulo'])
			i.articulo =  art
			i.existencia = self.request.POST['existencia']
			alm = Almacen.objects.get(pk = self.request.POST['almacen'])
			i.almacen = alm
			i.save() 
			#inv.save()
	
		form.instance.user = self.request.user
		return super(MovInv, self).form_valid(form)

 

 

	def form_invalid(self, form):
		#print self.request.POST['nivel']
		#print self.request.POST['existencia']
		#print self.request.POST['almacen']
		print 'no'
		return super(MovInv, self).form_invalid(form)

	def get_context_data(self, **kwargs):
		context = super(MovInv,self).get_context_data(**kwargs)
		context['articulos'] = Articulo.objects.all()  
		context['alma'] = Almacen.objects.all()
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
	queryset = Inventario.objects.filter(existencia__gt=0)
	paginate_by  = 7
	success_url = '/' 


	def get_context_data(self, **kwargs):
		context = super(ListInvMov,self).get_context_data(**kwargs)
		context['stock'] = Inventario.objects.aggregate(Sum('existencia')).values()[0]  
		#context['tt'] = Inventario.objects.aggregate(Sum('preciototal')).values()[0]
		return context



def Lista_InvAjax(request): 
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

def ArticuloCreatePopup(request):
	form = ArticuloForm(request.POST or None)
	if form.is_valid():
		form.instance.user = request.user
		instance = form.save()

		## Change the value of the "#id_author". This is the element id in the form
		
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_articulo");</script>' % (instance.pk, instance))
	
	return render(request, "articulo_form.html", {"form" : form})


def ArticuloEditPopup(request, pk = None):
	instance = get_object_or_404(Articulo, pk = pk)
	form = ArticuloForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.instance.user = request.user
		instance = form.save()
		print instance
		print instance.pk, instance
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_articulo");</script>' % (instance.pk, instance))
	return render(request, "articulo_form.html", {"form" : form})


@csrf_exempt
def get_articulo_id(request):
	if request.is_ajax():
		nombre = request.GET['nombre']
		articulo_id = Articulo.objects.get(nombre = nombre).id
		data = {'articulo_id':articulo_id,}
		return HttpResponse(json.dumps(data), content_type='application/json')
	return HttpResponse("/")
 

