from django.db import models

# Create your models here.

class Izvodac(models.Model):
    izvodac_ime=models.CharField(max_length=50)
    izvodac_prezime=models.CharField(max_length=50)
    datum_rođenja=models.DateField()
    dodatne_informacije_izvodaca=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.izvodac_prezime

class Album(models.Model):
    naziv_albuma=models.CharField(max_length=50)
    izvodac=models.ForeignKey(Izvodac, on_delete=models.CASCADE)
    godina_izdavanja_albuma=models.CharField(max_length=4, default='2021')
    dodatne_informacije_albuma=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.naziv_albuma

class Pjesma(models.Model):
    naziv_pjesme=models.CharField(max_length=50)
    izvodac=models.ForeignKey(Izvodac, on_delete=models.CASCADE)
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    godina_izdavanja_pjesme=models.CharField(max_length=4, default='2021')
    trajanje_pjesme=models.CharField(max_length=50)

    def __str__(self):
        return self.naziv_pjesme