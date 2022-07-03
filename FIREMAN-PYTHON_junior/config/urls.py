from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path, include
import requests
from pensamentos.views import PensadoresViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register(r'pensadores', PensadoresViewSet)


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include(router.urls)),
]