from django.contrib import admin
from .models import Surprises

# Register your models here.

class SurprisesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('surprise_name',)}
    list_display = ('surprise_name', 'slug')

admin.site.register(Surprises, SurprisesAdmin)