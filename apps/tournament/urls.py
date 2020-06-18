from django.urls import path
from .views import Fixtureview, HomeView


app_name = 'fixture'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('tournaments/<int:id>/', Fixtureview.as_view(), name="fixture"),
]
