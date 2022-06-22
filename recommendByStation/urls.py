from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/',views.index),
    path('csv2Model/',views.csv2Model),
    path('Beomnaegol/',views.Beomnaegol),
    path('Beomil/',views.Beomil),
    path('Jwacheon/',views.Jwacheon),
    path('Busanjin/',views.Busanjin),
    path('Choryang/',views.Choryang),
    path('BusanStation/',views.BusanStation),
    path('Jungang/',views.Jungang),
    path('Nampo/',views.Nampo),
    path('Jagalchi/',views.Jagalchi),
]
