import pandas as pd
import matplotlib.pyplot as plt

# Importing data (into Python) - atp_matches in 2022
# Cleaning data (optional/if needed) - Retrieving tourney id, name and surface type
data = pd.read_csv('atp_matches_2022.csv')

# Get total number of matches played with a 
# 25 year old or younger (win or lose)
youthListLosersTotal = data.query('loser_age <= 25')
youthListWinnersTotal= data.query('winner_age <= 25') 

# + 1 as programming starts at 0
totalMatchesWithYouth = len(youthListLosersTotal.index) + 1 + len(youthListWinnersTotal.index) + 1
print(f'Total number of matches with a 25 year old (or younger) : {totalMatchesWithYouth}')

# Get the probability plot of age winning under n={3,2,1} hour(s)

# take all of the under 2-hour long matches with 25 year olds and under who are winners
youthListWinnersUnderThreeHours = data.query('winner_age <= 25 & minutes<180')
youthListWinnersUnderThreeHours.to_csv('YouthWinnersUnderThreeHours')

# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
matchesWonUnderThreeHours = len(youthListWinnersUnderThreeHours.index) + 1
print(f'youth matches won under 3 hours: {matchesWonUnderThreeHours}')

# Get probability of winning a match under 2 hours
probabilityUnderThreeHours = matchesWonUnderThreeHours / totalMatchesWithYouth
probabilityUnderThreeHours = probabilityUnderThreeHours * 100
probabilityUnderThreeHours = round(probabilityUnderThreeHours, 2)
print(f'Probability of a 25 year old (or younger) winning a match under two hours: {probabilityUnderThreeHours}%')

# take all of the under 2-hour long matches with 25 year olds and under who are winners
youthListWinnersUnderTwoHours = data.query('winner_age <= 25 & minutes<120')
youthListWinnersUnderTwoHours.to_csv('YouthWinnersUnderTwoHours')

# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
matchesWonUnderTwoHours = len(youthListWinnersUnderTwoHours.index) + 1
print(f'youth matches won under 2 hours: {matchesWonUnderTwoHours}')

# Get probability of winning a match under 2 hours
probabilityUnderTwoHours = matchesWonUnderTwoHours / totalMatchesWithYouth
probabilityUnderTwoHours = probabilityUnderTwoHours * 100
probabilityUnderTwoHours = round(probabilityUnderTwoHours, 2)
print(f'Probability of a 25 year old (or younger) winning a match under two hours: {probabilityUnderTwoHours}%')

# take all of the under 1 hour long matches with 25 year olds and under who are winners
youthListWinnersUnderOneHour = data.query('winner_age <= 25 & minutes <= 60')
youthListWinnersUnderOneHour.to_csv('YouthWinnersUnderOneHour')

# Total num of matches won by >= 25 year old under 60 mins
# + 1 as programming starts at 0
matchesWonUnderOneHour = len(youthListWinnersUnderOneHour.index) + 1
print(f'youth matches won under 1 hour: {matchesWonUnderOneHour}')

# Get probability of winning a match under 2 hours
probabilityUnderOneHour = matchesWonUnderOneHour / totalMatchesWithYouth
probabilityUnderOneHour = probabilityUnderOneHour * 100
probabilityUnderOneHour = round(probabilityUnderOneHour, 2)
print(f'Probability of a 25 year old (or younger) winning a match under one hour: {probabilityUnderOneHour}%')

# Probability of 25 year olds (and under) winning a match
# Match Length        Probability
# Under 1 hour            n%
# Under 2 hours           n%
# Under 3 hours           n%

ProbabilityGraph = {'Match Length': ['Under 1 Hour', 'Under 2 Hours', 'Under 3 hours'],
                    'Probability of Youth Winning': [probabilityUnderOneHour, probabilityUnderTwoHours, probabilityUnderThreeHours]}
ProbabilityGraphDF = pd.DataFrame(ProbabilityGraph)
# print(ProbabilityGraphDF)
ProbabilityGraphDF.plot(x='Match Length', y='Probability of Youth Winning', kind='line') 

plt.show()