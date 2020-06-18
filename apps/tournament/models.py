from datetime import datetime, timedelta
from django.db import models

# Setting default 30 days
def now_plus_30():
	return datetime.now() + timedelta(days = 30)


class Tournament(models.Model):
	"""
	The tournament
	"""
	title = models.CharField(max_length=100)
	start_date = models.DateTimeField(auto_now_add=True, blank=True)
	end_date = models.DateTimeField(default=now_plus_30)

	def __str__(self):
		return self.title


class Venue(models.Model):
	"""
	Place of fixture
	"""
	name = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return self.name

