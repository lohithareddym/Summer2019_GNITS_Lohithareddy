from django.urls import path
from matchdetails.views import seasons
from matchdetails.views.login import LoginView, logout_view,loginwithmessage
urlpatterns=[
    path('seasons/',seasons.SeasonListView.as_view(),name='seasons_list'),
    path('seasons/<int:ssn>/',seasons.SeasonListView.as_view(),name='season'),
    path('matchdetails/<int:matchid>/',seasons.MatchDetails.as_view(),name='matchdetails'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/<int:matchid>/', LoginView.as_view(), name='login'),
    path('login_error/', loginwithmessage.as_view(), name='login_error'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),

]
