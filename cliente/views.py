from django.shortcuts import render
from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.core.context_processors import csrf

from django.contrib.auth.models import User
from producto.models import Product
from empleado.models import Empleado
from ordenes.models import OrdenProducto, Orden, Estatus
from .models import Cliente
from django.core import urlresolvers
import datetime
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

@login_required(login_url='/login/')
def clientes(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    clientes = Cliente.objects.order_by('-id')
    page_title = "Clientes"
    template ="clientes.html" 
    args = {'clientes': clientes, 'page_title': page_title, 'empleado': empleado}  
    return render_to_response(template, locals(),context_instance=RequestContext(request))

@login_required(login_url='/login/')
def cliente(request,cliente_id):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    cliente = get_object_or_404(Cliente, id=cliente_id)
    ordenes = Orden.objects.filter(cliente=cliente)
    page_title = "Cliente"
    template ="cliente.html"   
    return render_to_response(template, locals(),context_instance=RequestContext(request))
