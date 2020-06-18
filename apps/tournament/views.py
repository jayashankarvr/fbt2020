from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Tournament
from .forms import TournamentForm


class HomeView(FormView):
	""" Home View - list and add tournament"""
	template_name = 'index.html'
	form_class = TournamentForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['form'] = self.form_class
		tours = Tournament.objects.all()
		context['tournaments'] = tours
		return context

	def form_valid(self, form):
		if form.is_valid:
			form.save()
		return super().form_valid(form)
