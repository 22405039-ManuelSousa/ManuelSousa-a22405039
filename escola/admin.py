from django.contrib import admin

# Register your models here.

from .models import Escola

class EscolaAdmin(admin.ModelAdmin):
    list_display = ("nome", "alunos",)
    ordering = ("nome", "alunos",)
    search_fields = ("nome",)
    editable_fields = ("alunos",)
    
# Register your models here.
admin.site.register(Escola, EscolaAdmin)