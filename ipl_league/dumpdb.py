import click
import openpyxl
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',"ipl_league.settings")
django.setup()
from matchdetails.models import Matches,Deliveries


def get_data(sheet):
    rangeSelected = []
    for row in sheet.iter_rows():
        rowSelected = []
        for cell in row:
            rowSelected.append(cell.value)
        if(rowSelected!=None):
            rangeSelected.append(rowSelected)
    return rangeSelected
@click.group()
def commands():
     pass
@commands.command(short_help="create a new database")
@click.argument("matches_excel")
#@click.argument("deliveries_excel"),deliveries_excel
def importdata(matches_excel):
    # read data from matches.csv
    workbook_1 = openpyxl.load_workbook(matches_excel)
    sheet_obj_1 = workbook_1.get_sheet_by_name("Worksheet")
    data = get_data(sheet_obj_1)[1:]
    for i in range(len(data)):
        obj = Matches(id=data[i][0],season=data[i][1],city=data[i][2],date=data[i][3],team1=data[i][4],team2 =data[i][5],toss_winner=data[i][6],
                      toss_decision =data[i][7],result=data[i][8],dl_applied=data[i][9],winner=data[i][10],win_by_runs=data[i][11],
                      win_by_wickets = data[i][12],player_of_match=data[i][13],venue=data[i][14],umpire1=data[i][15],umpire2=data[i][16],umpire3=data[i][17])
        obj.save()
commands()