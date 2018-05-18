from django.shortcuts import render, Http404
from .models import Person, ZeitKorrektur

# Create your views here.

def index(request):
    titel = "Hello World"
    context = {'titel' : titel}

    return render(request, 'index.html', context)

def detail(request, pers_nr):

    name = Person.objects.get(pers_nr=pers_nr).nach_name
    text = "Hier stehen die Korrekturen von {}".format(name)
    blabla = "Blabla"
    try:
        corrections = ZeitKorrektur.objects.select_related().filter(person=pers_nr)
    except Zeitkorrektur.DoesNotExist:
        raise Http404("Zeitkorrektur nicht vorhanden")
    
    context = {
        'text' : text,
        'blabla' : blabla,
        'corrections' : corrections,
    }

    return render(request, 'detail.html', context)