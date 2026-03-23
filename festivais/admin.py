from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Festival

class FestivalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'local')
    search_fields = ('nome', 'local')
    list_filter = ('local',)

admin.site.register(Festival, FestivalAdmin)