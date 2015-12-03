from django.conf.urls import url
from . import views

 
urlpatterns = [
    url(r'^addventa/$', views.AddVenta.as_view(),name='add_venta'),  
    url(r'^listventa/$',views.ListaVenta.as_view(),name='list_vta'),
    url(r'^listcobro/$', views.ListCobro.as_view(),name ='list_cobro'),
    url(r'^listvtahoy/$',views.ListVentahoy.as_view(),name='list_vtahoy'),
    #url(r'^addcobro/$',views.AddCobro.as_view(),name='add_cobro'),
    url(r'^cxcdet/(?P<pk>\d+)/$',views.CxcDetalle.as_view(),name='det_cxc'),
   # url(r'^buscanombre_url/$','apps.venta.views.ListaAlumnos_ajax',name='aj_busanombre'),
    url(r'^auto/$','apps.venta.views.persona_auto_complete', name='persona_auto_complete'),
    url(r'^ajax-listexis/$','apps.venta.views.InvExisAjax'),

 
    
]
 