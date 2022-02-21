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

def dodavanje_albuma(request):
    form = AlbumForm()
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/albumi_create.html', context=context)

def dodavanje_pjesme(request):
    form = PjesmaForm()
    if request.method == "POST":
        form = PjesmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/izvodaci")

    context = {"form": form}
    return render(request, 'admin/pjesme_create.html', context=context)

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