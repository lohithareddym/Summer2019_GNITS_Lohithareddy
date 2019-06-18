from django.urls import path
from matchdetails.views import seasons

urlpatterns=[
    path('seasons/',seasons.SeasonListView.as_view(),name='seasons_list'),
    path('seasons/<int:ssn>/',seasons.SeasonListView.as_view(),name='season'),
    path('matchdetails/<int:matchid>/',seasons.MatchDetails.as_view(),name='matchdetails'),
]
