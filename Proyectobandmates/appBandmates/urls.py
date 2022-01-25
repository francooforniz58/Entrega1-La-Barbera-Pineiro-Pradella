from django.urls import path
from appBandmates.views import *

urlpatterns = [
    path('', inicio, name = "inicio")
]