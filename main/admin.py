from django.contrib import admin

from main.models import *

class MappingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Mapping, MappingAdmin)
