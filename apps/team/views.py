from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404

from .models import Team, Fixture
from .forms import TeamForm
from apps.user.forms import CustomUserCreationForm



class Teamview(FormView):
	""" Team View - list and add teams"""
	template_name = 'teams.html'
	form_class = TeamForm
	success_url = 'teams/'

	def get_context_data(self, **kwargs):
		context = super(Teamview, self).get_context_data(**kwargs)
		teams = Team.objects.all().count()
		if teams <= 10:
			context['form'] = self.form_class
		return context

	def form_valid(self, form):
		if form.is_valid:
			form.save()
		teams = Team.objects.all().count()
		if teams == 10:
			self.create_first_round()
		return super().form_valid(form)


	def create_first_round(self):
		""" Only 4 teams for first round id 10 teams"""
		fixture = Fixture()
		first_round_teams = Team.objects.all()[:4]
		fixture.title="Round 1 A"
		fixture.tournament = first_round_teams[0].tournament
		fixture.a_team = first_round_teams[0]
		fixture.b_team = first_round_teams[1]
		fixture.date_time = tournament.start_date
		fixture.venue = Venue.objects.first()
		fixture.save()

		fixture2 = Fixture()
		fixture2.title="Round 1 B"
		fixture2.tournament = first_round_teams[0].tournament
		fixture2.a_team = first_round_teams[2]
		fixture2.b_team = first_round_teams[3]
		fixture2.date_time = tournament.start_date
		fixture2.venue = Venue.objects.first()
		fixture2.save()


class TeamDetailView(FormView):
	""" Add, view members """
	template_name = 'teams-detail.html'
	form_class = CustomUserCreationForm
	success_url = 'teams/'

	def get_context_data(self, **kwargs):
		context = super(TeamDetailView, self).get_context_data(**kwargs)
		context['form'] = self.form_class
		return context

	def form_valid(self, form):
		if form.is_valid:
			form.save()
		return super().form_valid(form)