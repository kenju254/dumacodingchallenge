from django.contrib import admin

from places import models

class CountyAdmin(admin.ModelAdmin):
    pass

class WardAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.County, CountyAdmin)
admin.site.register(models.Ward, WardAdmin)
admin.site.register(models.Location, LocationAdmin)