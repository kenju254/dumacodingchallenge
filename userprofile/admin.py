from django.contrib import admin

from userprofile import models

'''Profile Model on Admin Site'''
class ProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Profile, ProfileAdmin)