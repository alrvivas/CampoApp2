from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^add-buena/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_buena',name='add_devolucion_buena'),
	url(r'^add-mala/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_mala',name='add_devolucion_mala'),
	url(r'^add-mala-almacen/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_mala_almacen',name='add_devolucion_mala_almacen'),
	url(r'^add-reproceso/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_reproceso',name='add_devolucion_reproceso'),
	url(r'^add-reproceso-almacen/(?P<producto_slug>[-\w]+)/$', 'devoluciones.views.add_devolucion_reproceso_almacen',name='add_devolucion_reproceso_almacen'),
	url(r'^buenas/$', 'devoluciones.views.devoluciones_buenas',name='devoluciones_buenas'),
	url(r'^buena/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_buena',name='devolucion_buena'),
	url(r'^malas/$', 'devoluciones.views.devoluciones_malas',name='devoluciones_malas'),
	url(r'^malas-almacen/$', 'devoluciones.views.devoluciones_malas_almacen',name='devoluciones_malas_almacen'),
	url(r'^mala/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_mala',name='devolucion_mala'),
	url(r'^mala-almacen/(?P<devolucion_almacen_id>[-\w]+)/$', 'devoluciones.views.devolucion_mala_almacen',name='devolucion_mala_almacen'),
	url(r'^reprocesos/$', 'devoluciones.views.devoluciones_reproceso',name='devoluciones_reproceso'),
	url(r'^reprocesos-almacen/$', 'devoluciones.views.devoluciones_reproceso_almacen',name='devoluciones_reproceso_almacen'),
	url(r'^reproceso/(?P<devolucion_id>[-\w]+)/$', 'devoluciones.views.devolucion_reproceso',name='devolucion_reproceso'),
	url(r'^reproceso-almacen/(?P<devolucion_almacen_id>[-\w]+)/$', 'devoluciones.views.devolucion_reproceso_almacen',name='devolucion_reproceso_almacen'),
	
	
) 