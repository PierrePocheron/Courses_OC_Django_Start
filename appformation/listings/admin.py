from django.contrib import admin
from listings.models import *

# Documentation : Import every table class
# https://stackoverflow.com/questions/9443863/register-every-table-class-from-an-app-in-the-django-admin-page

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band', 'year')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
