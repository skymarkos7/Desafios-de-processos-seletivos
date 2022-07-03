from django.http.response import HttpResponse, JsonResponse
import requests
from rest_framework import viewsets
from pensamentos.models import Pensador
from pensamentos.serializer import PensadorSerializer



class PensadoresViewSet(viewsets.ModelViewSet):
    queryset = Pensador.objects.all()
    serializer_class = PensadorSerializer
