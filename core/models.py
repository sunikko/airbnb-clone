from django.db import models


class TimeStampModel(models.Model):

    """Time Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    # it's Abstract not go into db /Meta means extra infomation
    class Meta:
        abstract = True
