from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView
from .models import Venta, Cxc
from apps.principal.models import Articulo,Inventario,Cliente
from .forms import VentaForm,CobroForm
from django.views.generic.edit import FormMixin

from datetime import date
import decimal
from django.db.models import Q
from django.http import HttpResponse
import json as simplejson
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import redirect

class AddVenta(CreateView):
	form_class = VentaForm
	models = Venta
	template_name = 'venta_form.html'
	success_url  = '/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(AddVenta, self).form_valid(form) 

 	def form_invalid(self, form):
 		return super(AddVenta, self).form_invalid(form)

 	def get_form(self, form_class):
 		form = super(AddVenta, self).get_form(form_class)
 		form.fields['inventario'].queryset = Inventario.objects.filter(almacen__virtual=True)
 		return form
 
 	def post(self, request, *args, **kwargs):
 		post = super(AddVenta, self).post(request, *args, **kwargs)
 		a = self.request.POST['inventario']
 		i = Inventario.objects.get(pk = a)
 	 	i.existencia = i.existencia - int(self.request.POST['cantidad'])
 		i.save()
 	 	
		art  = Articulo.objects.get(pk= i.articulo.id)
		prec = self.request.POST['cantidad']
		tot = art.precio * decimal.Decimal(prec)
		eng = self.request.POST['enganche']
		tot = decimal.Decimal(tot) - decimal.Decimal(eng)
		vta = Venta.objects.get(pk=self.object.id)
		usr = self.request.user
		fechax = request.POST['apartir']
		fecha = datetime.strptime(fechax, '%d/%m/%Y')
		cxc = Cxc(user=usr,venta=vta,total=tot,proxcobro=fecha,saldo=tot,tipo=100)
		cxc.save()
		cxc = Cxc(user=usr,venta=vta,saldo=tot,proxcobro=fecha,tipo=200)
		cxc.save()
		return post


class ListaVenta(ListView):
	context_object_name = 'ventas'
	template_name = 'list_venta.html'
	queryset = Venta.objects.all().order_by('-fecha')
	paginate_by  = 7
	success_url = '/'


class ListCobro(ListView):
	 context_object_name = 'cobros'
	 template_name = 'cobro_list.html'
	 today = date.today()
	 queryset = Cxc.objects.filter(proxcobro__lte=today,tipo=200,pagado=False,status=False).order_by('proxcobro')


class ListVentahoy(ListView):
	context_object_name = 'ventas'
	template_name = 'list_venta.html'
	model = Venta 						 

	def get_queryset(self):
		today = date.today()
		return super(ListVentahoy, self).get_queryset().filter(fechaventa__year=today.year,
			fechaventa__month=today.month,fechaventa__day=today.day) 

	 



class CxcDetalle(FormMixin,DetailView):
	model = Cxc
	form_class = CobroForm
	context_object_name = 'cxc'
	template_name = 'cobro_det.html'
	success_url  = '/'

	def get_context_data(self, **kwargs):
		context = super(CxcDetalle, self).get_context_data(**kwargs)
		context['form'] = self.get_form(self.form_class)
		cxc = Cxc.objects.get(id = self.object.id)
		context['pagos'] = Cxc.objects.filter(venta = cxc.venta.id)
		return context

 	def post(self, request, *args, **kwargs):
 		self.object = self.get_object()
 		self.form = self.get_form(self.form_class)

 		if self.form.is_valid():
 			return self.form_valid(self.form)
 		else:
 			return self.form_invalid(self.form)

 	def form_valid(self, form):
 		today = date.today()
		saldoanterior = Cxc.objects.filter(id = self.object.id).latest('pk') # con latest obtiene el ultimo pk es lo mismo que order -id[0], y con earliest['pk'] se obtiene el primero
		fechax = self.request.POST['proxcobro']
		fecha = datetime.strptime(fechax, '%d/%m/%Y')

		upcxc = Cxc.objects.get(id = self.object.id)
		upcxc.abono = self.request.POST['abono']
		upcxc.fechaabono = today
		upcxc.saldo = saldoanterior.saldo - decimal.Decimal(self.request.POST['abono'])
		upcxc.pagado = True
		SaldoActual = saldoanterior.saldo - decimal.Decimal(self.request.POST['abono'])
		if SaldoActual == 0 : # pene en true el status  ya  no debe  nada 
			upcxc.status = True
		upcxc.save()


		if SaldoActual > 0 :
			c = Cxc()
			cxc = Cxc.objects.get(id = self.object.id)
			c.user = self.request.user
	 		c.venta = Venta.objects.get(id=cxc.venta.id)
	 		c.proxcobro =  fecha
	 		c.saldo = saldoanterior.saldo - decimal.Decimal(self.request.POST['abono'])
	 		c.tipo = 200
	 		c.save()
	 	return super(CxcDetalle, self).form_valid(form)

 	def form_invalid(self, form):
 		return super(CxcDetalle, self).form_invalid(form)
 
 

def persona_auto_complete(request):
	#q = request.REQUEST['term']
	q = request.GET.get('term','')
 	if q:
  		qset = (
   		Q(nombre__icontains=q)    		
   	)
  		personas = Cliente.objects.filter(qset).distinct()
  		personas_list = []
 	else:
  		personas = []
 		personas_list = []

 	for p in personas:
  		value = '%s, (%s)' % (p.nombre,p.calle+' '+ p.numero)
  		p_dict = {'id': p.id, 'label': value, 'value': value}
  		personas_list.append(p_dict)
 	return HttpResponse(simplejson.dumps(personas_list))

def InvExisAjax(request):
	if request.is_ajax():
		i = Inventario.objects.get(id = request.GET['id'])
		response = JsonResponse({'existencia': i.existencia})
		return HttpResponse(response.content)
	else:
		return redirect('/')
