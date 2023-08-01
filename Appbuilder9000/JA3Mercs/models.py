from django.db import models


class Merc(models.Model):
    fname = models.CharField(max_length=60, default="", blank=True, null=False)
    lname = models.CharField(max_length=60, default="", blank=True, null=False)
    callsign = models.CharField(max_length=60, default="", blank=True, null=False)
    description = models.CharField(max_length=300, default="", blank=True, null=False)
    salary = models.DecimalField(max_digits=20, decimal_places=2, default="", blank=True, null=False)
    image = models.CharField(max_length=255, default="", blank=True)