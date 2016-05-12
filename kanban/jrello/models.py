from django.db import models


class Jrello(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(null=True, blank=True)
