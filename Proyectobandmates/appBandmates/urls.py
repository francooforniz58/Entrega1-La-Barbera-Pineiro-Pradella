from django.urls import path
from appBandmates.views import *

urlpatterns = [
    path('', inicio, name = "inicio"),
    path('musicos/', musicos, name="musicos"),
    path('bandas/', bandas, name="bandas" ),
    path('managers/', managers, name="managers"),
]