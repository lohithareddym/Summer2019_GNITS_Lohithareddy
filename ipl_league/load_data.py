import os
import django
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"ipl_league.settings")
django.setup()
from matchdetails.models import *
with open('deliveries.csv','rt') as f:
    data=csv.DictReader(f)
    for row in data:
        match=Deliveries(**row)
        match.save()