from django.http import HttpResponse,HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response,get_object_or_404, render,redirect
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.db.models import Count, Avg,Sum
from django.views.generic.base import View
from django.utils import timezone

from salidas.models import Salida
from devoluciones.models import DevolucionBuena,DevolucionReproceso,DevolucionMala
from empleado.models import Empleado
from models import *
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q  

def LoginView(request):
    if not request.user.is_anonymous():
        return redirect('index')
    if request.POST:
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return redirect('index')
                else:
                    return render_to_response('inactivousuario.html', context_instance=RequestContext(request))#no activo
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))#no usuario
    else:
        formulario = AuthenticationForm()
    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def index(request):
    page_title      = "Control de Inventarios"
    now             = timezone.now()
    user        = request.user
    empleado    = Empleado.objects.filter(user= user)
    salidas         = Salida.objects.filter(fecha_de_salida=datetime.datetime.today).aggregate(Sum('cantidad'))
    salidas_k       = Salida.objects.filter(fecha_de_salida=datetime.datetime.today)      
    devoluciones_kb  = DevolucionBuena.objects.filter(fecha_de_entrada=datetime.datetime.today)
    devoluciones_km  = DevolucionMala.objects.filter(fecha_de_salida=datetime.datetime.today)
    devoluciones_kr  = DevolucionReproceso.objects.filter(fecha_de_entrada=datetime.datetime.today)
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(fecha_de_salida__icontains=query)
        )
        qset2 = (
            Q(fecha_de_entrada__icontains=query)
        )
        qset3 = (
            Q(fecha_de_salida__icontains=query)
        )
        qset4 = (
            Q(fecha_de_entrada__icontains=query)
        )
        results = Salida.objects.filter(qset).aggregate(Sum('cantidad'))
        salidas_kr      = Salida.objects.filter(qset)
        devoluciones_br = DevolucionBuena.objects.filter(qset2).aggregate(Sum('cantidad'))
        devoluciones_kbr = DevolucionBuena.objects.filter(qset2)
        devoluciones_mr = DevolucionMala.objects.filter(qset3).aggregate(Sum('cantidad'))
        devoluciones_kmr = DevolucionMala.objects.filter(qset3)
        devoluciones_rr = DevolucionReproceso.objects.filter(qset4).aggregate(Sum('cantidad'))
        devoluciones_krr = DevolucionReproceso.objects.filter(qset4)
        template_name   = "searchi.html"
        args2           = {'empleado':empleado,'results': results,'query': query,'devoluciones_kmr':devoluciones_kmr,'devoluciones_krr':devoluciones_krr,'devoluciones_kbr':devoluciones_kbr,'salidas_kr':salidas_kr,'devoluciones_br':devoluciones_br,'devoluciones_mr':devoluciones_mr,'devoluciones_rr':devoluciones_rr,}
        return render_to_response(template_name, args2,context_instance=RequestContext(request))
    else:
        results = []  
    template ="index.html" 
    args            = {}
    args            = {'page_title':page_title,'salidas':salidas,'salidas_k':salidas_k,'empleado':empleado,}
    return render_to_response(template, args,context_instance=RequestContext(request))

