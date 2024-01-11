from django.shortcuts import render
from django.http import HttpResponse

def contato(request):
    return HttpResponse('Contato')

def home(request):
    return render(request, 'recipes/home.html')