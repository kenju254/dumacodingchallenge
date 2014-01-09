from django.contrib import admin

from places.models import *

'''County Model on Admin'''
class CountyAdmin(admin.ModelAdmin):
    pass

'''Ward Model on Admin'''
class WardAdmin(admin.ModelAdmin):
    pass

'''Location Model on Admin'''
class LocationAdmin(admin.ModelAdmin):
    pass


admin.site.register(County, CountyAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Location, LocationAdmin)