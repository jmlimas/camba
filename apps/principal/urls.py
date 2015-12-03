from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^$',views.IndexView.as_view(),name='index'), 
    url(r'^addarticulo/$', views.AddArticulo.as_view(),name='add_articulo'), 
    url(r'^listarticulo/$',views.ListArticulos.as_view(),name='list_articulos'),
    url(r'^updatearticulo/(?P<pk>\d+)/$',views.UpdateArticulo.as_view(),name='update_articulo'),
    url(r'^addubica/$', views.AddAlmacen.as_view(),name='add_ubicacion'),
    url(r'^listubica/$',views.ListAlmacen.as_view(),name='list_ubicacion'),
    url(r'^updateubica/(?P<pk>\d+)/$',views.UpdateAlmacen.as_view(),name='update_ubicacion'),
    url(r'^addinve/$', views.AddRecibo.as_view(),name='add_inventario'),
    url(r'^listinv/$',views.ListInv.as_view(),name='list_inventario'),
    url(r'^listinvmov/$',views.ListInvMov.as_view(),name='list_invmov'),
    url(r'^addcliente/$', views.AddCliente.as_view(),name='add_cliente'),
    url(r'^listcliente/$', views.ListCliente.as_view(),name='list_cliente'),
    url(r'^updatecliente/(?P<pk>\d+)/$',views.UpdateCliente.as_view(),name = 'update_cliente'),
    url(r'^addvendedor/$', views.AddVendedor.as_view(),name='add_vendedor'),
    url(r'^listvendedor/$',views.ListVendedor.as_view(),name = 'list_vendedor'),
    url(r'^updatevendedor/(?P<pk>\d+)/$', views.UpdateVendedor.as_view(),name='update_vendedor'),
    url(r'^addmovinv/$',views.MovInv.as_view(),name='add_movinv'),
    url(r'^ajax/lisinv/$',"apps.principal.views.Lista_InvAjax"),
 
]