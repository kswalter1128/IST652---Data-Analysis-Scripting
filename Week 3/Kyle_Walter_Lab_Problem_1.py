#%%
import os
os.chdir('R:\Graduate School\IST652 - Data Analytics Scripting\Week 3')

#read the file
nbafile = open('NBA-Attendance-1989.txt', 'r')

#munge the data
nbalist =[]
for i in nbafile:
    textline = i.strip()
    items = textline.split()
    nbalist.append(items)
nbafile.close()
#Breaks teh variables into their own lists
teams=[]
attend=[]
prices=[]
for (team, attendance, price) in nbalist:
    teams.append(team)
    attend.append(int(attendance))
    prices.append(float(price))
#Outputs a readable sentence for each team
for a,b,c in zip(teams,attend,prices):
    line="The attendance at {} was {:,} and the ticket price was ${:.2f}."
    print(line.format(a,b,c))