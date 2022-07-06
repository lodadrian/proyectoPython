from email.errors import NoBoundaryInMultipartDefect
from django.http import HttpResponse
from django.shortcuts import render
from AppAdrian.models import Familia
from django.shortcuts import HttpResponse
# Create your views here.

def fam(self):

    familia=Familia(nombre="Adrian",apellido="Gomez",tlf=988127372,fecha="2002-07-02")
    familia2=Familia(nombre="Luis",apellido="Sanchez",tlf=984823123,fecha="2003-08-13")
    familia3=Familia(nombre="Juan",apellido="Perez",tlf=983823211,fecha="2004-09-14")

    texto=f"Familiar creado: {familia.nombre} {familia.apellido} {familia.tlf} {familia.fecha}"
    texto2=f"Familiar creado: {familia2.nombre} {familia2.apellido} {familia2.tlf} {familia2.fecha}"
    texto3=f"Familiar creado: {familia3.nombre} {familia3.apellido} {familia3.tlf} {familia3.fecha}"

    return HttpResponse(texto+"<br>"+texto2+"<br>"+texto3)