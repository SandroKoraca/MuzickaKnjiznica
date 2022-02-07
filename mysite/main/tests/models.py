from django.test import TestCase
from main.models import *


class Testmodels(TestCase):

    def setUp(self):
        self.izvodac1 = Izvodac.objects.create(
            izvodac_ime = 'TestIme',
            izvodac_prezime = 'TestPrezime',
            datum_rođenja = '1998-05-05',
            dodatne_informacije_izvodaca = 'TestInformacijeIzvodaca'
        )

        self.album1 = Album.objects.create(
            naziv_albuma = 'TestAlbum',
            izvodac = 'TestPrezime',
            godina_izdavanja_albuma = '2020',
            dodatne_informacije_albuma = 'TestInformacijeAlbuma'
        )

        self.pjesma1 = Pjesma.objects.create(
            naziv_pjesme = 'TestPjesma',
            album = 'TestAlbum',
            godina_izdavanja_pjesme = '2020',
            trajanje_pjesme = '3:42'
        )

    def test_izvodac(self):
        self.assertEquals(self.izvodac1.izvodac_prezime, "TestPrezime")

    def test_album(self):
        self.assertEquals(self.album1.naziv_albuma, "TestAlbum")
    
    def test_pjesma(self):
        self.assertEquals(self.pjesma1.naziv_pjesme, "TestPjesma")
