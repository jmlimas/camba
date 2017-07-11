from django.conf.urls import  url
from . import views


urlpatterns = [ 
    url(r'^login/$',  'apps.users.views.userlogin',name='login'), 
    url(r'^change/$', 'apps.users.views.change_password',name='change'),
    url(r'^salir/$',  'apps.users.views.LogOut', name = 'logout'),
]
