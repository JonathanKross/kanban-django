from django.db import models


class Card(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	priority = models.CharField(max_length=255)
	status = models.CharField(max_length=255)

	def __str__(self):
		return self.name
