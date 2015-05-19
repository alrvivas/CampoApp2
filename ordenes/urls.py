from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^orden-exitosa/(?P<orden_id>[-\w]+)$', 'ordenes.views.orden_exitosa', name='orden-exitosa'), 
	url(r'^orden/(?P<orden_id>[-\w]+)$', 'ordenes.views.orden', name='orden'), 
	url(r'^$', 'ordenes.views.crear_orden', name='crear-orden'), 
	url(r'^ordenes-pendientes/$', 'ordenes.views.ordenes_pendientes', name='ordenes-pendientes'),
	url(r'^orden-pendiente/(?P<orden_id>[-\w]+)$', 'ordenes.views.orden_pendiente', name='orden-pendiente'), 
	url(r'^ordenes-entregadas/$', 'ordenes.views.ordenes_entregadas', name='ordenes-entregadas'),
)