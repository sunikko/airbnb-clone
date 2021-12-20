from django.contrib import admin
from . import models


# admin.site.register(models.User, CustomUserAmdin)
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """
    list_diaplay = ('username', 'gender', 'language', 'currency', 'superhost')
