from django.db import models
from django.contrib.auth.models import AbstractUser
from ..team.models import Team


class CustomUser(AbstractUser):
	""" 
	Custom fields for team member 
	"""
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	is_coach = models.BooleanField(default=False)
	is_manager = models.BooleanField(default=False)

	def __str__(self):
		return self.username