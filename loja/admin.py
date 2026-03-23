from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)
    list_filter = ('preco',)

admin.site.register(Produto, ProdutoAdmin)