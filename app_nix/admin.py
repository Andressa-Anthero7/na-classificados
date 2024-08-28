from django.contrib import admin
from .models import Leads, AnuncioVeiculo, Anunciante, Tagmeta, TagGoogle, Cores, TagGoogleBody

# Register your models here.

admin.site.register(Leads)
admin.site.register(AnuncioVeiculo)
admin.site.register(Anunciante)
admin.site.register(Tagmeta)
admin.site.register(TagGoogle)
admin.site.register(TagGoogleBody)
admin.site.register(Cores)

