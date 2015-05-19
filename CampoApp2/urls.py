from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CampoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^catalogo/', include('producto.urls')),
    url(r'^checkout/', include('direccion.urls')),
    url(r'^salidas/', include('salidas.urls')),
    url(r'^produccion/', include('produccion.urls')),
    url(r'^devolucion/', include('devoluciones.urls')),
    url(r'^saldo/', include('saldo_anterior.urls')),
    url(r'^orden/',include('ordenes.urls')),
    url(r'^$', 'empleado.views.index', name='index'), 
    url(r'^login/$', 'empleado.views.LoginView', name='login'),
    url(r'^logout/$', 'empleado.views.LogoutView', name='logout'),
    url(r'^cliente/', include('cliente.urls')),   
    
)
handler404 = 'productos.views.file_not_found_404' 
if settings.DEBUG == False:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
   )