from django.contrib import admin

# Register your models here.
from mapping.models import Traveler, Location, Annotate, List

admin.site.register(Traveler)
admin.site.register(Location)
admin.site.register(Annotate)
admin.site.register(List)