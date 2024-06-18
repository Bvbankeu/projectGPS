from django.db import models
from datetime import datetime

# Create your models here.
class GpsModule(models.Model):

    #date_add = models.DateTimeField(auto_now_add=True)
    id     = models.CharField(primary_key=True, max_length=16)
    #IMEI = models.CharField(max_length=16)
    battery     = models.FloatField()
    simNumber    = models.CharField(max_length=15)
    idEnfant = models.IntegerField()
    status = models.IntegerField()
    
    def __unicode__(self):
        return "{0}".format(self.code)

class GpsCoordinates(models.Model):

    date = models.DateTimeField()
    gpsModule = models.ForeignKey('GpsModule', related_name="gps_coordinates", on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude  = models.FloatField()
   
    def __unicode__(self):
        return "{0}".format(self.code)
    
    def date_conversion(date):
        year = int(date[0:2], 16) + 2000  # Ajouter 2000 pour obtenir l'année complète
        month = int(date[2:4], 16)
        day = int(date[4:6], 16)
        hour = int(date[6:8], 16)
        minute = int(date[8:10], 16)
        second = int(date[10:12], 16)

        # Créer un objet datetime
        dt = datetime(year, month, day, hour, minute, second)

        return dt

    def coordinates_conversion(coordinate):
        coordinate = int(coordinate, 16)
        coordinate = coordinate/30000
        coordinate_int_part = (coordinate // 60)
        coordinate_decimal_part = (coordinate - coordinate_int_part*60)/60
        coordinate = coordinate_int_part + coordinate_decimal_part
        return coordinate