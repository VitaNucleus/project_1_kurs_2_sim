from django.db import models


class River(models.Model):
    name = models.CharField(max_length=100)
    area = models.FloatField()
    price = models.FloatField()
    rent = models.BooleanField(default=False)
