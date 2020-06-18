from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .models import Tournament
from .forms import TournamentForm
from django.shortcuts import get_object_or_404
from .models import Team
from .forms import FixtureForm

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



class Fixtureview(FormView):
	""" Team View - list and add teams"""
	template_name = 'fixtures.html'
	form_class = FixtureForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(Fixtureview, self).get_context_data(**kwargs)
		print(kwargs)
		context['form'] = self.form_class
		# tour = get_object_or_404(Tournament, id=kwargs['id'])
		# context['teams'] = tour.fixtures	
		return context

	def form_valid(self, form):
		if form.is_valid:
			form.save()
		return super().form_valid(form)


class CreateFixture(TemplateView):

	def create_fixture(self):
		""" For 10 teams, first round should be a fixture of four teams """
		get_four = Team.objects.all()[:4]
		get_date = 