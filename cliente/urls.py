from django.conf.urls import patterns, include, url
#from .views import ShopListView
#from .views import ProductDetailView
#from .models import Product

urlpatterns = patterns('',
	url(r'^$', 'cliente.views.clientes', name='clientes'), 
	url(r'^cliente/(?P<cliente_id>[-\w]+)$', 'cliente.views.cliente', name='cliente'), 

)