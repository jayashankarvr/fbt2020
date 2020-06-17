from django.db import models


class Tournament(models.Model):
	"""
	The tournament
	"""
	title = models.CharField(max_length=100)
	start_date = models.DateTimeField()
	End_date = models.DateTimeField()

	def __str__(self):
		return self.title