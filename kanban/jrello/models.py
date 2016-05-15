from django.db import models
from django.contrib.auth.models import User

class Jrello(models.Model):

    PRIORITY_CHOICES = [(1, "High"), (2, "Moderate"), (3, "Low")]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_CHOICES, null=True, blank=True)
    last_edited = models.DateTimeField(auto_now=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
