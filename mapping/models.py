from django.contrib.auth.models import AbstractUser
from django.db import models
from geopy.geocoders import Nominatim


class Traveler(AbstractUser):
    current_location = models.CharField(max_length=40, null=True)
    
    def __unicode__(self):
        return u"{}".format(self.username)

class Location(models.Model):
    city_state = models.CharField(max_length=30)

    def lat(self):
        geolocator = Nominatim()
        location = geolocator.geocode(self.city_state)
        latitude = location.latitude
        return latitude

    def lon(self):
        geolocator= Nominatim()
        location = geolocator.geocode(self.city_state)
        longitude = location.longitude
        return longitude
    
    def __unicode__(self):
        return u"{}".format(self.city_state)

class Annotate(models.Model):
    comment = models.CharField(max_length=5000)
    photo = models.ImageField(upload_to='images', blank=True, null=True)
    location = models.ForeignKey(Location, related_name='annotation_location')
    user = models.ForeignKey(Traveler, related_name='annotation_traveler')

    def __unicode__(self):
        return u"{} {}".format(self.comment, self.user)


class List(models.Model):
    list_name = models.CharField(max_length=32, default='')
    user = models.ForeignKey(Traveler, related_name='list_traveler')
    locations = models.ManyToManyField(Location, related_name='list_locations')

    def __unicode__(self):
        return u"{}".format(self.list_name)



