from django.urls import path
from . import views
from main.views import AlbumList, IzvodacList, PjesmaList
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path('', views.o_nama, name='homepage'),
    path('izvodaci/', IzvodacList.as_view()),
    path('izvodaci/<izvodaci>', AlbumList.as_view()),
    path('izvodaci/<izvodaci>/<album>', PjesmaList.as_view())
]

urlpatterns += staticfiles_urlpatterns()