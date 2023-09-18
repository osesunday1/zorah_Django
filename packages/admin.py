from django.contrib import admin
from .models import Packages

# Register your models here.

class PackagesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('package_name',)}
    list_display = ('package_name', 'slug')

admin.site.register(Packages, PackagesAdmin)