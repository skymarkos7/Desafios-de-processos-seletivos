from django.contrib import admin
from pensamentos.models import Pensador

class Pensadores(admin.ModelAdmin):
    list_display = ('id', 'autor', 'fala')
    list_display_links = ('id', 'autor')
    search_fields = ('autor',)

   

admin.site.register(Pensador, Pensadores)    

