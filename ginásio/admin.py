from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'plano')
    search_fields = ('nome',)
    list_filter = ('plano',)

admin.site.register(Cliente, ClienteAdmin)