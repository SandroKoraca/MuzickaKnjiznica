from django.urls import path
from . import views
from main.views import AlbumList, IzvodacList, PjesmaList, admin_panel
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.o_nama, name='homepage'),
    
    path('izvodaci/', IzvodacList.as_view()),
    path('izvodaci/DodavanjeIzvodaca', views.dodavanje_izvodaca, name='homepage'),
    path('izvodaci/<izvodaci>/UredivanjeIzvodaca', views.uredivanje_izvodaca, name='homepage'),
    path('izvodaci/<izvodaci>/BrisanjeIzvodaca', views.brisanje_izvodaca, name='homepage'),

    path('izvodaci/<izvodaci>', AlbumList.as_view()),
    path('izvodaci/<izvodaci>/DodavanjeAlbuma', views.dodavanje_albuma, name='homepage'),
    path('izvodaci/<izvodaci>/<album>/UredivanjeAlbuma', views.uredivanje_albuma, name='homepage'),
    path('izvodaci/<izvodaci>/<album>/BrisanjeAlbuma', views.brisanje_albuma, name='homepage'),

    path('izvodaci/<izvodaci>/<album>', PjesmaList.as_view()),
    path('izvodaci/<izvodaci>/<album>/DodavanjePjesme', views.dodavanje_pjesme, name='homepage'),
    path('izvodaci/<izvodaci>/<album>/<pjesma>/UredivanjePjesme', views.uredivanje_pjesme, name='homepage'),
    path('izvodaci/<izvodaci>/<album>/<pjesma>/BrisanjePjesme', views.brisanje_pjesme, name='homepage'),

    path('adminpanel/', views.admin_panel, name='homepage'),
    path('adminpanel/DodavanjeAlbuma', views.dodavanje_albuma_novi, name='homepage'),
]

urlpatterns += staticfiles_urlpatterns()