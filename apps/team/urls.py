from django.urls import path
from apps.team.views import Teamview


app_name = 'team'
urlpatterns = [
    path('<int:id>/', Teamview.as_view(), name="teams"),
]
