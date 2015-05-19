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
from .models import OrdenProducto, Orden, Estatus
from cliente.models import Cliente
from .forms import ordenForm, ordenproductoForm
from producto.forms import stockForm
from django.core import urlresolvers
import datetime
from django.db.models import Q
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory


@login_required(login_url='/login/')
def orden_exitosa(request,orden_id):
    user = request.user
    empleado = Empleado.objects.filter(user=user)
    orden = get_object_or_404(Orden, id=orden_id)
    productos = OrdenProducto.objects.filter(orden=orden)
    page_title = "Orden Exitosa"
    template = "orden-exitosa.html"
    args = {'productos': productos, 'page_title': page_title, 'empleado': empleado}
    return render_to_response(template, locals(), context_instance=RequestContext(request))


@login_required(login_url='/login/')
def ordenes_entregadas(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    ordenes = Orden.objects.order_by('-id')
    page_title = "Ordenes Entregadas"
    template ="ordenes-entregadas.html"   
    return render_to_response(template, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def orden(request,orden_id):
    user = request.user
    empleado = Empleado.objects.filter(user=user)    
    productos = Product.objects.all()
    status = Estatus.objects.all()
    orden = get_object_or_404(Orden, id=orden_id)
    cliente = Cliente.objects.filter()
    OrdenProductoFormSet = modelformset_factory(OrdenProducto,form=ordenproductoForm,extra=len(productos))
    if request.method == 'POST':
        formorden = ordenForm(request.POST, instance=orden)
        formset = OrdenProductoFormSet(request.POST, request.FILES)
        if formorden.is_valid() and formset.is_valid():
            formset.save()
            orden = formorden.save(commit=False)
            orden.save()
            return redirect(orden.get_absolute_urle())
    else:
        formset = OrdenProductoFormSet(queryset=OrdenProducto.objects.none())
        formorden = ordenForm()
    args = {}
    args.update(csrf(request))
    page_title = "Capturar Orden"
    return render_to_response('orden.html', locals(), context_instance=RequestContext(request))


@login_required(login_url='/login/')
def crear_orden(request):
    user = request.user
    empleado = Empleado.objects.filter(user=user)
    cliente = Cliente.objects.all()
    status = Estatus.objects.all()
    orden = Orden.objects.all()
    if request.POST:
        form = ordenForm(request.POST)
        if form.is_valid():
            orden = form.save(commit=False)
            orden.save()
        return redirect(orden.get_absolute_url())
    else:
        form = ordenForm()
    args = {}
    args.update(csrf(request))
    page_title = "Crear Orden"
    template = "crear-orden.html"
    args = {'user': user, 'status': status, 'form': form, 'orden': orden, 'page_title': page_title,
            'empleado': empleado, 'cliente': cliente}
    return render_to_response(template, locals(), context_instance=RequestContext(request))

@login_required(login_url='/login/')
def ordenes_pendientes(request):
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    ordenes = Orden.objects.order_by('-id')
    page_title = "Ordenes Por Entregar"
    template ="ordenes-por-entregar.html"   
    return render_to_response(template, locals(),context_instance=RequestContext(request)) 

@login_required(login_url='/login/')
def orden_pendiente(request,orden_id):
    user = request.user
    empleado = Empleado.objects.filter(user=user)    
    status = Estatus.objects.all()
    orden = get_object_or_404(Orden, id=orden_id)
    productos = Product.objects.all()
    productoso = OrdenProducto.objects.filter(orden=orden)
    ProductoFormSet = modelformset_factory(Product,form=ordenproductoForm,extra=0)
    if request.method == 'POST':
        formorden = ordenForm(request.POST, instance=orden)
        formset = ProductoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            form = formorden.save(commit = False)
            form.save()
            return redirect('ordenes-pendientes')
    else:
        formset = ProductoFormSet()
        formorden = ordenForm()
    args = {}
    args.update(csrf(request))
    page_title = "Orden Pendiente"
    template = "orden-pendiente.html"
    return render_to_response(template, locals(), context_instance=RequestContext(request))