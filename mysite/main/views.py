from main.models import Album, Izvodac, Pjesma
from django.shortcuts import render, redirect    
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login    
from .forms import *

## Create your views here.
def homepage(request):
    return render(request, 'base_generic.html')

def o_nama(request):
    return render(request, 'o_nama.html')

def admin_panel(request):
    return render(request, 'admin_panel.html')

def dodavanje_izvodaca(request):
    form = IzvodacForm()
    if request.method == "POST":
        form = IzvodacForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/izvodaci_create.html', context=context)

def uredivanje_izvodaca(request, izvodaci):
    odabrani_izvodac = Izvodac.objects.get(izvodac_prezime=izvodaci)
    form = IzvodacForm(instance=odabrani_izvodac)
    if request.method == "POST":
        form = IzvodacForm(request.POST, instance=odabrani_izvodac)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/izvodaci_create.html', context=context)

def brisanje_izvodaca(request, izvodaci):
    odabrani_izvodac = Izvodac.objects.get(izvodac_prezime=izvodaci)

    if request.method == "POST":
        odabrani_izvodac.delete()
        return redirect("/izvodaci")

    context = {"izvodac": odabrani_izvodac}
    return render(request, "admin/izvodaci_delete.html", context)

def dodavanje_albuma(request, izvodaci):
    initial_dict = {
        "izvodac": izvodaci
    }
    form = AlbumForm(initial = initial_dict)
    if request.method == "POST":
        form = AlbumForm(request.POST, initial = initial_dict)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci/"+izvodaci)

    context = {"form": form}
    return render(request, 'admin/albumi_create.html', context=context)

def dodavanje_albuma_novi(request):
    form = AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/albumi_create.html', context=context)

def uredivanje_albuma(request, izvodaci, album):
    odabrani_album = Album.objects.get(naziv_albuma=album)
    form = AlbumForm(instance=odabrani_album)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=odabrani_album)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci/"+izvodaci)

    context = {"form": form}
    return render(request, 'admin/albumi_create.html', context=context)
    
def brisanje_albuma(request, izvodaci, album):
    odabrani_album = Album.objects.get(naziv_albuma=album)

    if request.method == "POST":
        odabrani_album.delete()
        return redirect("/izvodaci/"+izvodaci)

    context = {"album": odabrani_album}
    return render(request, "admin/albumi_delete.html", context)

def dodavanje_pjesme(request, izvodaci, album):
    initial_dict = {
        "album": album
    }
    form = PjesmaForm(initial = initial_dict)
    if request.method == "POST":
        form = PjesmaForm(request.POST, initial = initial_dict)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci/"+izvodaci+"/"+album)

    context = {"form": form}
    return render(request, 'admin/pjesme_create.html', context=context)

def dodavanje_pjesme_nova(request):
    form = PjesmaForm()
    if request.method == "POST":
        form = PjesmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/pjesme_create.html', context=context)

def uredivanje_pjesme(request, izvodaci, album, pjesma):
    odabrana_pjesma = Pjesma.objects.get(naziv_pjesme=pjesma)
    form = PjesmaForm(instance=odabrana_pjesma)
    if request.method == "POST":
        form = PjesmaForm(request.POST, instance=odabrana_pjesma)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci/"+izvodaci+"/"+album)

    context = {"form": form}
    return render(request, 'admin/pjesme_create.html', context=context)
    
def brisanje_pjesme(request, izvodaci, album, pjesma):
    odabrana_pjesma = Pjesma.objects.get(naziv_pjesme=pjesma)

    if request.method == "POST":
        odabrana_pjesma.delete()
        return redirect("/izvodaci/"+izvodaci+"/"+album)

    context = {"pjesma": odabrana_pjesma}
    return render(request, "admin/pjesme_delete.html", context)

class IzvodacList(ListView):
    model = Izvodac

class AlbumList(ListView):
    template_name = 'main/album_list.html'

    def get_queryset(self):
        self.izvodac = get_object_or_404(Izvodac, izvodac_prezime=self.kwargs['izvodaci'])
        return Album.objects.filter(izvodac=self.izvodac)

class PjesmaList(ListView):
    template_name = 'main/pjesma_list.html'

    def get_queryset(self):
        self.album = get_object_or_404(Album, naziv_albuma=self.kwargs['album'])
        return Pjesma.objects.filter(album=self.album)