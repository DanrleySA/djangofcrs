from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'evento/home.html', {
        'nome': 'Danrley SA',
        'idade': '19 anos',
        'altura': '1,83 metros',
        })
