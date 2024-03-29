from django.shortcuts import render, redirect

from django.http import HttpResponse

from studenci.models import Miasto, Uczelnia

from django.contrib import messages

from django.urls import reverse

from studenci.forms import UserLoginForm, UczelniaForm, MiastoForm


def index(request):
    return HttpResponse("<h1>Witaj wsród sudentów!</h1>")
    # return render(request,'pizza/index.html')


def miasta(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        form = MiastoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            m = Miasto(nazwa=form.cleaned_data['nazwa'], kod=form.cleaned_data['kod'])
            m.save()
            messages.success(request, "poprawnie dodano dane!")
            return redirect(reverse('studenci:miasta'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = MiastoForm

    miasta = Miasto.objects.all()
    kontekst = {'miasta': miasta, 'form': form}
    return render(request, 'studenci/miasta.html', kontekst)

def uczelnie(request):
    """Widok wyświetlający miasta i formularz ich dodawania"""
    if request.method == 'POST':
        form = UczelniaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            u = Uczelnia(nazwa=form.cleaned_data['nazwa'])
            u.save()
            messages.success(request, "Poprawnie dodano dane!")
            return redirect(reverse('studenci:uczelnie'))
        else:
            messages.error(request, "Niepoprawne dane!")
    else:
        form = UczelniaForm

    uczelnie = Uczelnia.objects.all()
    kontekst = {'uczelnie': uczelnie, 'form': form}
    return render(request, 'studenci/uczelnie.html', kontekst)


def loguj_studenta(request):
    if request.method == 'POST':
        pass
    else:
        form = UserLoginForm()
    kontekst = {'form': form}
    return render(request, 'studenci/login.html', kontekst)
