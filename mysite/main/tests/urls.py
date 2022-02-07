from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import homepage, AlbumList, IzvodacList, PjesmaList, o_nama


class TestUrls(SimpleTestCase):

    def test_homepage_url_is_resolved(self):
        url = reverse('')
        # print(resolve(url))

        self.assertEquals(resolve(url).func, o_nama)

    def test_izvodaci_url_is_resolved(self):
        url = reverse('izvodaci/')

        self.assertEquals(resolve(url).func.view_class, IzvodacList)

    def test_album_url_is_resolved(self):
        url = reverse('izvodaci/<izvodaci>', args=['TestPrezime'])

        self.assertEquals(resolve(url).func.view_class, AlbumList)

    def test_authors_url_is_resolved(self):
        url = reverse('izvodaci/TestPrezime/<album>', args=['TestAlbum'])

        self.assertEquals(resolve(url).func.view_class, PjesmaList)
