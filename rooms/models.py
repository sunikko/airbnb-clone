from django.db import models


class Room(models.Model):
    """ Room Model Definition """
    created = models.DateTimeField()
    update = models.DateTimeField()
