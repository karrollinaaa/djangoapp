from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Witaj w aplikacji Studenci!</h1>")
    #return render(request, 'pizza/index.html')

def komunikat(request):
    return HttpResponse("<h1>Nowości od studentów!</h1>")
    #return render(request, 'pizza/komunikat.html')

