from django.db import models
from ..tournament.models import Tournament, Venue

class Team(models.Model):
	"""
	Tournament Team model
	"""
	name = models.CharField(max_length=50)
	description = models.TextField(null=True, blank=True)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams', null=True)

	def __str__(self):
		return self.name


class Fixture(models.Model):
	"""
	The match between two teams
	"""
	title = models.CharField(max_length=100)
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="fixtures")
	a_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="a_fixture")
	b_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="b_fixture")
	venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
	date_time = models.DateTimeField()

	def __str__(self):
		return self.title
