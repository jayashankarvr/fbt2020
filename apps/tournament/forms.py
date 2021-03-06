from django.forms import ModelForm, DateInput
from .models import Tournament
from apps.team.models import Fixture


class TournamentForm(ModelForm):
	""" Fixed start date and end date """
	class Meta:
		model = Tournament
		exclude = ['start_date', 'end_date',]


class FixtureForm(ModelForm):
	"""  """
	class Meta:
		model = Fixture
		exclude = []