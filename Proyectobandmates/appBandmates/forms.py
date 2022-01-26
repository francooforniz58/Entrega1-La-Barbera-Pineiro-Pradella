from django import forms

class MusicoFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    edad = forms.IntegerField()
    genero = forms.CharField() 
    email= forms.EmailField()

class BandaFormulario(forms.Form):
    nombre= forms.CharField()
    genero = forms.CharField() 
    integrantes = forms.IntegerField()
    email= forms.EmailField()

class ManagerFormulario(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    edad = forms.IntegerField()
    numero = forms.IntegerField()
    email= forms.EmailField()