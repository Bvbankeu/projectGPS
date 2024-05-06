from django.db import models

# Create your models here.
class GpsModule(models.Model):

    #date_add = models.DateTimeField(auto_now_add=True)
    id     = models.IntegerField(primary_key=True)
    battery     = models.FloatField()
    simNumber    = models.CharField(max_length=15)
    idEnfant = models.IntegerField()
    
    def __unicode__(self):
        return "{0}".format(self.code)

class GpsCoordinates(models.Model):

    date = models.DateTimeField()
    gpsModule = models.ForeignKey('GpsModule', related_name="gps_coordinates", on_delete=models.CASCADE)
    longitude = models.FloatField()
    latitude  = models.FloatField()
   
    def __unicode__(self):
        return "{0}".format(self.code)

