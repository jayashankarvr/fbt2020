from django.db import models



class Team(models.Model):
	"""
	Tournament Team model
	"""

	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.name