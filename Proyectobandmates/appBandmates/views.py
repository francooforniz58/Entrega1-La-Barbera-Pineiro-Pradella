
from django.shortcuts import render
from django.http import HttpResponse
from appBandmates.models import *
from appBandmates.forms import *

def inicio(request):

    return render(request, "appBandmates/inicio.html")

def musicos(request):

    lista = Musico.objects.all()
    return render(request, "appBandmates/musicos.html",{"lista":lista})

def bandas(request):
    
    return render(request, "appBandmates/bandas.html")

def managers(request):
    
    return render(request, "appBandmates/managers.html")

def musicos(request):
    
    if request.method == 'POST':

        miFormulario = MusicoFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            musico = Musico(nombre=informacion['nombre'], edad=informacion['edad'], genero=informacion['genero'], email=informacion['email']) 

            musico.save()

            return render(request, "appBandmates/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= MusicoFormulario() #Formulario vacio para construir el html

    return render(request, "appBandmates/musicos.html", {"miFormulario":miFormulario})

def bandas(request):
    
    if request.method == 'POST':

        miFormulario = BandaFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            banda = Banda(nombre=informacion['nombre'],genero=informacion['genero'],integrantes=informacion['integrantes'], email=informacion['email']) 

            banda.save()

            return render(request, "appBandmates/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= BandaFormulario() #Formulario vacio para construir el html

    return render(request, "appBandmates/bandas.html", {"miFormulario":miFormulario})

def managers(request):
    
    if request.method == 'POST':

        miFormulario = ManagerFormulario(request.POST) #aquí mellega toda la información del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si pasó la validación de Django

            informacion = miFormulario.cleaned_data

            manager = Manager(nombre=informacion['nombre'], edad=informacion['edad'], numero=informacion['numero'], email=informacion['email']) 

            manager.save()

            return render(request, "appBandmates/inicio.html") #Vuelvo al inicio o a donde quieran
    else: 

        miFormulario= ManagerFormulario() #Formulario vacio para construir el html

    return render(request, "appBandmates/managers.html", {"miFormulario":miFormulario})

def busquedaNombre(request):
    
    return render(request, "appBandmates/busquedaNombre.html")

def buscar(request):
    #respuesta = f"Estamos buscando el usuario con nombre: {request.GET['nombre']}"
    if  request.GET["nombre"]:

        nombre =request.GET["nombre"]
        musicos = Musico.objects.filter(nombre__incontains=nombre)
        return render(request, "appBandmates/resultadosBusqueda.html", {"nombre":nombre, "musicos":musicos})
    
    else:
        respuesta = "no enviaste datos"

    return HttpResponse(respuesta)

