from django.db import models
#from
# Create your models here.
class Matches(models.Model):
    id=models.IntegerField(primary_key=True)
    season=models.IntegerField()
    city=models.CharField(null=True,max_length=501)
    date=models.DateField(null=True,blank=True)
    team1=models.CharField(null=True,max_length=30)
    team2 = models.CharField(null=True,max_length=30)
    toss_winner=models.CharField(null=True,max_length=30)
    toss_decision = models.CharField(null=True,max_length=10)
    result=models.CharField(null=True,max_length=10)
    dl_applied=models.BooleanField(null=True,default=0)
    winner=models.CharField(null=True,max_length=30)
    win_by_runs=models.IntegerField(null=True)
    win_by_wickets = models.IntegerField(null=True)
    player_of_match=models.CharField(null=True,max_length=50)
    venue=models.CharField(null=True,max_length=80)
    umpire1=models.CharField(null=True,max_length=50)
    umpire2=models.CharField(null=True,max_length=50)
    umpire3=models.CharField(max_length=50,null=True,blank=True)
    def __int__(self):
        return self.id
class Deliveries(models.Model):
    inning=models.IntegerField()
    batting_team=models.CharField(null=True,max_length=50)
    bowling_team=models.CharField(null=True,max_length=50)
    over=models.IntegerField(null=True,)
    ball=models.IntegerField(null=True,)
    batsman=models.CharField(null=True,max_length=50)
    non_striker=models.CharField(null=True,max_length=50)
    bowler=models.CharField(null=True,max_length=50)
    is_super_over=models.BooleanField(null=True,default=0)
    wide_runs=models.IntegerField(null=True)
    bye_runs=models.IntegerField(null=True)
    legbye_runs = models.IntegerField(null=True)
    noball_runs=models.IntegerField(null=True)
    penalty_runs=models.IntegerField(null=True)
    batsman_runs=models.IntegerField(null=True)
    extra_runs=models.IntegerField(null=True)
    total_runs=models.IntegerField(null=True)
    player_dismissed=models.CharField(null=True,max_length=50)
    dismissal_kind=models.CharField(null=True,max_length=50)
    fielder=models.CharField(null=True,max_length=50)
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)