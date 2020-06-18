from django.forms import ModelForm, DateInput
from .models import Team


class TeamForm(ModelForm):
	"""  """
	class Meta:
		model = Team
		fields = ['name', 'description',]