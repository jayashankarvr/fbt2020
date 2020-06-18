from django.forms import ModelForm, DateInput
from .models import Tournament


class TournamentForm(ModelForm):
	""" Fixed start date and end date """
	class Meta:
		model = Tournament
		exclude = ['start_date', 'end_date',]