from django.db import models


class TimeStampModel(models.Model):

    """ Time Stamped Model """
    created = models.DateTimeField()
    update = models.DateTimeField()

    # it's Abstract not go into db
    class Meta:
        abstract = True
