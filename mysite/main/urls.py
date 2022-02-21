from django.urls import path
from . import views
from main.views import AlbumList, IzvodacList, PjesmaList, admin_panel
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.o_nama, name='homepage'),
    path('izvodaci/', IzvodacList.as_view()),
    path('izvodaci/<izvodaci>', AlbumList.as_view()),
    path('izvodaci/<izvodaci>/<album>', PjesmaList.as_view()),
    path('adminpanel/', views.admin_panel, name='homepage'),
    path('adminpanel/DodavanjeIzvodaca', views.dodavanje_izvodaca, name='homepage'),
    path('adminpanel/DodavanjeAlbuma', views.dodavanje_albuma, name='homepage'),
    path('adminpanel/DodavanjePjesme', views.dodavanje_pjesme, name='homepage'),
]

urlpatterns += staticfiles_urlpatterns()