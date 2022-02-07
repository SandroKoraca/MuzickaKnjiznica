from django.test import TestCase, Client
from django.urls import reverse
from main.models import *


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('')
        self.izvodaci_url = reverse('izvodaci/')
        self.album_url = reverse('izvodaci/<izvodaci>', args=['TestPrezime'])
        self.pjesma_url = reverse('izvodaci/TestPrezime/<album>', args=['TestAlbum'])

        self.izvodac1 = Izvodac.objects.create(
            izvodac_ime = 'TestIme',
            izvodac_prezime = 'TestPrezime',
            datum_rođenja = '1998-05-05',
            dodatne_informacije_izvodaca = 'TestInformacije'
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

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'o_nama.html')

    def test_project_izvodaci_GET(self):
        client = Client()

        response = client.get(self.izvodaci_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/izvodaci_list.html')
    
    def test_project_album_GET(self):
        client = Client()

        response = client.get(self.album_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/album_list.html')

    def test_project_pjesme_GET(self):
        client = Client()

        response = client.get(self.pjesma_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/pjesma_list.html')
