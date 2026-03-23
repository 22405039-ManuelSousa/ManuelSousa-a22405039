from django.contrib import admin
from .models import Receita

class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(Receita, ReceitaAdmin)