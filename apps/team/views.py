from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from .models import Team
from .forms import TeamForm


class Teamview(FormView):
	""" Team View - list and add teams"""
	template_name = 'teams.html'
	form_class = TeamForm
	success_url = 'teams/'

	def get_context_data(self, **kwargs):
		context = super(Teamview, self).get_context_data(**kwargs)
		context['form'] = self.form_class
		tour = get_object_or_404(Tournament, id=kwargs['id'])
		context['teams'] = tour.teams
		return context

	def form_valid(self, form):
		if form.is_valid:
			form.save()
		return super().form_valid(form)
