import csv

"""
Needs testing - File with all the games status
  - Phase 2 add type in case we need more information from other CSV.
"""
def readCSV(file):
  with open(file,"rb") as filename:
    details = csv.DictReader(filename, delimiter=',')
    data = [r for r in details] #compact information about all the games.
    # add for to create object for each row of the
    for i in range(len(data)):
      createMatchObject(data[i]) #creating the match object


def createMatchObject(data):
  print "---"
  print data["Date"]



readCSV("/Users/PauloCardoso/desktop/P1.csv")



"""
Div - Division
Date - Date
HomeTeam - HomeTeam
AwayTeam - AwayTeam
FTHG - Final Time Home Goals
FTAG - Final Time Away Goals,
FTR - (H)ome, (D)raw or (A)way,
HTHG - Home Team Halftime Goals,
HTAG - Away Team Halftime Goals,
HTR - Half Time Result,
HS - Home Shots,
AS - Away Shots,
HST - Home Shots Target,
AST - Away Shots Target,
HF - Home Fouls,
AF - Away Fouls,
HC - Home Cards,
AC - Away Cards,
HY - Yellow Cards Home,
AY - Yellow Cards Away,
HR - Red Cards Home,
AR - Red Cards Away,


Bets - ask Luis about them
B365H,B365D,B365A,BWH,BWD,BWA,IWH,IWD,IWA,LBH,LBD,LBA,PSH,PSD,PSA,WHH,WHD,WHA,VCH,VCD,VCA,Bb1X2,BbMxH,BbAvH,BbMxD,BbAvD,BbMxA,BbAvA,BbOU,BbMx>2.5,BbAv>2.5,BbMx<2.5,BbAv<2.5,BbAH,BbAHh,BbMxAHH,BbAvAHH,BbMxAHA,BbAvAHA,PSCH,PSCD,PSCA
"""
