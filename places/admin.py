from django.contrib import admin

from places import models

'''County Model on Admin'''
class CountyAdmin(admin.ModelAdmin):
    pass

'''Ward Model on Admin'''
class WardAdmin(admin.ModelAdmin):
    pass

'''Location Model on Admin'''
class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.County, CountyAdmin)
admin.site.register(models.Ward, WardAdmin)
admin.site.register(models.Location, LocationAdmin)