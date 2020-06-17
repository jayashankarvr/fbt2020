from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
	"""
	Create team member
	"""
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('team','is_coach','is_manager',)


class CustomUserChangeForm(UserChangeForm):
	"""
	Modify team member
	"""
	class Meta:
		model = CustomUser
		fields = ('team','is_coach','is_manager',)