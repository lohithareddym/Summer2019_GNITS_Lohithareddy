from django.core.paginator import Paginator
from django.db.models import *
from django.views import View
from matchdetails.models import Matches,Deliveries
from django.urls import resolve
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from matchdetails.forms import *
class SeasonListView(View):
    def get(self, request ,*args, **kwargs):
        seasons = Matches.objects.values('season').distinct()
        #print(seasons)
        season_list=[]
        for season in seasons:
            season_list.append(season['season'])
        if kwargs:
            season=Matches.objects.filter(season=kwargs['ssn'])
        else:
            season = Matches.objects.filter(season=2019)
        paginator = Paginator(season, 8)
        page = request.GET.get('page')
        season = paginator.get_page(page)

        #print('season:\n\n',season)
        return render(request,
                        template_name='seasons_list.html',
                        context={
                        'seasons':season_list,
                        'matches':season
                        }
                        )
class MatchDetails(View):
    def get(self, request ,*args, **kwargs):
        print(kwargs['matchid'])
        matche = Deliveries.objects.filter(match_id=kwargs['matchid']).values()
        innings1=[]
        innings2=[]
        for i in matche:
            if i['inning']==1:
                innings1.append(i)
            else:
                innings2.append(i)
        toprunners = Deliveries.objects.filter(match_id=kwargs.get('matchid')).values('batsman', 'batting_team').annotate(Sum('total_runs')).order_by('-total_runs__sum')[:3]
        topbowlers = Deliveries.objects.values('bowler', 'bowling_team').filter(match_id=kwargs.get('matchid')).exclude(dismissal_kind=None).annotate(Count('dismissal_kind')).order_by('-dismissal_kind__count')[:3]
        print('rs:',toprunners)
        print('bs:', topbowlers)
        return render(request,
                        template_name='match_details.html',
                        context={
                            'toprunners': toprunners,
                            'topbowlers':topbowlers,
                            'innings1':innings1,
                            'innings2':innings2,
                        }
                        )