from django.http import HttpResponse
from django.shortcuts import render

from .models import Tapahtuma

def etusivu(request):
    tapahtumat = Tapahtuma.objects.all()
    vastaus = "<html><ul>"
    for tapahtuma in tapahtumat:
        vastaus += "<li>" + tapahtuma.otsikko + "</li>"
    vastaus += "</ul></hmtl>"
    return HttpResponse(vastaus)
