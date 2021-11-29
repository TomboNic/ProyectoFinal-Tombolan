from functools import reduce
from django.core.checks.messages import Error
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import FanBasquet, FanFormula1, FanFutbol, FanVoley
from .forms import FutbolFormulario, VoleyFormulario, BasquetFormulario, Formula1Formulario

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html", {})

#BUSQUEDA-------------------------------------------
#DE-------------------------------------------------
#DATOS----------------------------------------------

def listaFutbol(request):
    nombre = None
    Error =  None
    if request.method =="GET": 
        nombre = request.GET.get("nombre", "")

        if nombre == " ":
             Fans = FanFutbol.objects.all()

        else: 
            try:
                 nombre = str(nombre)
                 Fans = FanFutbol.objects.filter(nombre=nombre)
            except:
                    Error = "Ingresá un texto, no otra cosa"

    Fans = FanFutbol.objects.all()
    return render(request, "AppCoder/listaFutbol.html", {"FansFu": Fans, "Error": Error})

def listaBasquet(request):
    nombre = None
    Error =  None
    if request.method =="GET": 
        nombre = request.GET.get("nombre", "")

        if nombre == "":
             Fans = FanBasquet.objects.all()

        else:    
            try:
                nombre = str(nombre)
                Fans = FanBasquet.objects.filter(nombre=nombre)
            except:
                Error = "Ingresá un texto, no otra cosa"

    Fans = FanBasquet.objects.all()
    return render(request, "AppCoder/listaBasquet.html", {"FansBa": Fans, "Error": Error})

def listaF1(request):
    nombre = None
    Error =  None
    if request.method =="GET": 
        nombre = request.GET.get("nombre", "")

        if nombre == "":
             Fans = FanFormula1.objects.all()

        else:  
            try:
                nombre = str(nombre)
                Fans = FanFormula1.objects.filter(nombre=nombre)
            except:
                Error = "Ingresá un texto, no otra cosa"

    Fans = FanFormula1.objects.all()
    return render(request, "AppCoder/listaF1.html", {"FansF1": Fans, "Error": Error})

def listaVoley(request):
    nombre = None
    Error =  None
    if request.method =="GET": 
        nombre = request.GET.get("nombre", "")

        if nombre == "":
             Fans = FanVoley.objects.all()

        else:
            try:
                nombre = str(nombre)
                Fans = FanVoley.objects.filter(nombre=nombre)
            except:
                Error = "Ingresá un texto, no otra cosa"

    Fans = FanVoley.objects.all()
    return render(request, "AppCoder/listaVoley.html", {"FansVo": Fans, "Error": Error})

#CREACION----------------------------------------------------------
#DE----------------------------------------------------------------
#DATOS-------------------------------------------------------------

def crear_futbol(request):

    if request.method == "POST":
        formulario = FutbolFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            guardar = FanFutbol(Nombre=datos["Nombre"], equipo=datos["equipo"])
            guardar.save()
            return redirect("FanFutbol")
            
    formulario = FutbolFormulario()
    return render(request, "AppCoder/formFutbol.html", {"formulario": formulario})


def crear_voley(request):

    if request.method == "POST":
        formulario = VoleyFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            guardar = FanVoley(Nombre=datos["Nombre"], equipo=datos["equipo"])
            guardar.save()
            return redirect("FanVoley")
            
    formulario = VoleyFormulario()
    return render(request, "AppCoder/formVoley.html", {"formulario": formulario})

def crear_f1(request):

    if request.method == "POST":
        formulario = Formula1Formulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            guardar = FanFutbol(Nombre=datos["Nombre"], escuderia=datos["escuderia"])
            guardar.save()
            return redirect("FanF1")
            
    formulario = Formula1Formulario()
    return render(request, "AppCoder/formF1.html", {"formulario": formulario})

def crear_basquet(request):

    if request.method == "POST":
        formulario = BasquetFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data
            guardar = FanBasquet(Nombre=datos["Nombre"], equipo=datos["equipo"])
            guardar.save()
            return redirect("FanBasquet")
            
    formulario = BasquetFormulario()
    return render(request, "AppCoder/formBasquet.html", {"formulario": formulario})

