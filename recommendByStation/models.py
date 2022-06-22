from django.db import models

# Create your models here.
class StationInfo(models.Model):

    stationNum = models.IntegerField(default=0,primary_key=True)
    stationKor = models.CharField(max_length=100)
    stationEng = models.CharField(max_length=100)
    stationTel = models.CharField(max_length=50, default='')
    stationBikeStorage = models.BooleanField(default=False)
    stationItemStorage = models.BooleanField(default=False)
    stationTip = models.CharField(max_length=200)

    def __str__(self):
        return self.stationKor