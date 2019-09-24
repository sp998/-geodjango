from django.contrib.gis import admin
from .models import WorldBorder
from leaflet.admin import LeafletGeoAdmin


# Register your models here.
class Iadmin(LeafletGeoAdmin):
    list_display = ['name', 'location']


admin.site.register(WorldBorder, Iadmin)
