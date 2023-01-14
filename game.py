#BASEBALL SIMULATOR 0.1a
from random import randrange
import team1
import team2
function inning(None):
   break
innings = 9
inning = 1

battingteam1 = team1.x
pitchingteam1 = team1.y
bullpenteam1 = team1.z

battingteam2 = team2.x
pitchingteam2 = team2.y
bullpenteam2 = team2.z

team11 = randrange(100)
team12 = team11 - pitchingteam2 - bullpenteam2
team13 = team12 + battingteam1*2
team14 = team13/innings
team15 = round(team14/innings)
if team15 <= 0:
    team15 = 0

team21 = randrange(100)
team22 = team21 - pitchingteam1 - bullpenteam1
team23 = team22 + battingteam2*2
team24 = team23/innings
team25 = round(team24/innings)
if team25 <= 0:
    team25 = 0