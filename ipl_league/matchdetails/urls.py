from django.urls import path
from matchdetails.views import seasons
from matchdetails.views.login import LoginView, logout_view,loginwithmessage
from matchdetails.views.contact import emailView,successView
urlpatterns=[
#   seasons list
    path('seasons/',seasons.SeasonListView.as_view(),name='seasons_list'),
    path('seasons/<int:ssn>/',seasons.SeasonListView.as_view(),name='season'),
#   match details
    path('matchdetails/<int:matchid>/',seasons.MatchDetails.as_view(),name='matchdetails'),
#  login
    path('login/', LoginView.as_view(), name='login'),
    path('login/<int:matchid>/', LoginView.as_view(), name='login'),
    path('login_error/', loginwithmessage.as_view(), name='login_error'),
    path('signin/', LoginView.as_view(), name='signin'),
    path('logout/', logout_view, name='logout'),
# contact
    path('email/', emailView.as_view, name='email'),
    path('success/', successView.as_view, name='success'),

]
