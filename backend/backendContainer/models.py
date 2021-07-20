from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

class Animals(models.Model):
    '''Animals'''
    animalId = models.AutoField(primary_key=True)    
    animalLat = models.FloatField()
    animalLon = models.FloatField()
    animalOwn = models.CharField(max_length=256)
    animalCreatedAt = models.DateTimeField(default=timezone.now)
    animalUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_animal(self):
        '''function to update the date of CountryUpdatedAt field'''
        self.animalUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about Animals'''
        return self.animalId


class Deforestations(models.Model):
    '''Deforestation areas'''
    deforId = models.AutoField(primary_key=True)    
    deforLat = models.FloatField()
    deforLon = models.FloatField()
    deforArea = models.IntegerField(max_length=256)
    deforCreatedAt = models.DateTimeField(default=timezone.now)
    deforUpdatedAt = models.DateTimeField(default=timezone.now)

    def update_defor(self):
        '''function to update the date of CountryUpdatedAt field'''
        self.deforUpdatedAt = timezone.now()
        self.save()

    def __str__(self):
        '''customers info about Animals'''
        return self.deforId
