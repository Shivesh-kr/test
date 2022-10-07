from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
     title = models.CharField(max_length=100)
     location = models.CharField(max_length=100)
     pincode = models.IntegerField()
     incharge = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
     lat = models.CharField(max_length=255)
     lon = models.CharField(max_length=255)
     contact = models.CharField(max_length=12)

     is_active = models.BooleanField(default=True)
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now=True)

     def __str__(self):
         return self.title + self.location


class Crime(models.Model):
     robbery = 1
     fraud = 2
     child_ab = 3
     murder = 4
     cyber_c = 5
     TYPE_CHOICES = (
         (robbery, 'Robbery'),
         (fraud, 'Fraud'),
         (child_ab , 'Child Abuse'),
         (murder , 'Murder'),
         (cyber_c , 'Cyber Crime'),
     )

     reported_by         = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
     reported_on         = models.DateTimeField(auto_now_add=True)
     image               = models.ImageField(upload_to='crime_images/')
     station             = models.ForeignKey(Station, on_delete=models.PROTECT, null=True, blank=True)
     description         = models.TextField()
     lat                 = models.CharField(max_length=255)
     lon                 = models.CharField(max_length=255)
     type                = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, null=True, blank=True)
     reviewd             = models.BooleanField(default=False)
     created_on          = models.DateTimeField(auto_now_add=True)
     updated_on          = models.DateTimeField(auto_now=True)

     def __str__(self):
         return str(self.reported_by) + ' Reported cime on' + str(self.reported_on) + ' @ ' + str(self.station)