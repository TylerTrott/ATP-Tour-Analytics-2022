import pandas as pd
import matplotlib.pyplot as plt

# • Importing data (into Python) - atp_matches in 2022
# • Cleaning data (optional/if needed) - Retrieving tourney id, name and surface type
data = pd.read_csv('atp_matches_2022.csv')

print('What are the probabilties of different age groups winning an ATP tour tournament match under specific time ranges?')
print('')
#
# 25 year old and younger stats
#
print('25 year old and younger stats')

# Get total number of matches played with a
# 25 year old or younger (win or lose)
youthListLosersTotal = data.query('loser_age <= 25')
youthListWinnersTotal = data.query('winner_age <= 25')

# + 1 as programming starts at 0
totalMatchesWithYouth = len(youthListLosersTotal.index) + \
    1 + len(youthListWinnersTotal.index) + 1
print(
    f'Total number of matches with a 25 year old (or younger) : {totalMatchesWithYouth}')

# Get the probability plot of age winning under n={3,2,1} hour(s)

# take all of the under 2-hour long matches with 25 year olds and under who are winners
youthListWinnersUnderThreeHours = data.query('winner_age <= 25 & minutes<180')

# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
youthMatchesWonUnderThreeHours = len(youthListWinnersUnderThreeHours.index) + 1
print(f'Youth matches won under 3 hours: {youthMatchesWonUnderThreeHours}')

# Get probability of winning a match under 2 hours
youthProbabilityUnderThreeHours = youthMatchesWonUnderThreeHours / totalMatchesWithYouth
youthProbabilityUnderThreeHours = youthProbabilityUnderThreeHours * 100
youthProbabilityUnderThreeHours = round(youthProbabilityUnderThreeHours, 2)
print(
    f'Probability of a 25 year old (or younger) winning a match under two hours: {youthProbabilityUnderThreeHours}%')

# take all of the under 2-hour long matches with 25 year olds and under who are winners
youthListWinnersUnderTwoHours = data.query('winner_age <= 25 & minutes<120')
# Test output from query

# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
youthMatchesWonUnderTwoHours = len(youthListWinnersUnderTwoHours.index) + 1
print(f'youth matches won under 2 hours: {youthMatchesWonUnderTwoHours}')

# Get probability of winning a match under 2 hours
youthProbabilityUnderTwoHours = youthMatchesWonUnderTwoHours / totalMatchesWithYouth
youthProbabilityUnderTwoHours = youthProbabilityUnderTwoHours * 100
youthProbabilityUnderTwoHours = round(youthProbabilityUnderTwoHours, 2)
print(
    f'Probability of a 25 year old (or younger) winning a match under two hours: {youthProbabilityUnderTwoHours}%')

# take all of the under 1 hour long matches with 25 year olds and under who are winners
youthListWinnersUnderOneHour = data.query('winner_age <= 25 & minutes <= 60')


# Total num of matches won by >= 25 year old under 60 mins
# + 1 as programming starts at 0
youthMatchesWonUnderOneHour = len(youthListWinnersUnderOneHour.index) + 1
print(f'Youth matches won under 1 hour: {youthMatchesWonUnderOneHour}')

# Get probability of winning a match under 2 hours
youthProbabilityUnderOneHour = youthMatchesWonUnderOneHour / totalMatchesWithYouth
youthProbabilityUnderOneHour = youthProbabilityUnderOneHour * 100
youthProbabilityUnderOneHour = round(youthProbabilityUnderOneHour, 2)
print(
    f'Probability of a 25 year old (or younger) winning a match under one hour: {youthProbabilityUnderOneHour}%')

#
# 25 - 30 (30-exclusive) year old stats
#
print('')
print('25 - 30 (30-exclusive) year old stats:')

# Get total number of matches played with a
# 25-29 year old (win or lose)
midListLosersTotal = data.query('25 <= loser_age < 30')
midListWinnersTotal = data.query('25 <= winner_age < 30')

# + 1 as programming starts at 0
totalMatchesWithMid = len(midListLosersTotal.index) + \
    1 + len(midListWinnersTotal.index) + 1
print(f'Total number of matches with a 25-29 year old: {totalMatchesWithMid}')

# Get the probability plot of age winning under n={3,2,1} hour(s)

# take all of the under 2-hour long matches with 25 year olds and under who are winners
midListWinnersUnderThreeHours = data.query(
    '25 <= winner_age < 30 & minutes<180')


# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
midMatchesWonUnderThreeHours = len(midListWinnersUnderThreeHours.index) + 1
print(f'Mid matches won under 3 hours: {midMatchesWonUnderThreeHours}')

# Get probability of winning a match under 2 hours
midProbabilityUnderThreeHours = midMatchesWonUnderThreeHours / totalMatchesWithMid
midProbabilityUnderThreeHours = midProbabilityUnderThreeHours * 100
midProbabilityUnderThreeHours = round(midProbabilityUnderThreeHours, 2)
print(
    f'Probability of a 25-30 year old winning a match under two hours: {midProbabilityUnderThreeHours}%')

# take all of the under 2-hour long matches with 25 year olds and under who are winners
midListWinnersUnderTwoHours = data.query('25 <= winner_age < 30 & minutes<120')

# Total num of matches won by >= 25 year old under 120 mins
# + 1 as programming starts at 0
midMatchesWonUnderTwoHours = len(midListWinnersUnderTwoHours.index) + 1
print(f'Middle aged matches won under 2 hours: {midMatchesWonUnderTwoHours}')

# Get probability of winning a match under 2 hours
midProbabilityUnderTwoHours = midMatchesWonUnderTwoHours / totalMatchesWithMid
midProbabilityUnderTwoHours = midProbabilityUnderTwoHours * 100
midProbabilityUnderTwoHours = round(midProbabilityUnderTwoHours, 2)
print(
    f'Probability of a 25-30 year old winning a match under two hours: {midProbabilityUnderTwoHours}%')

# take all of the under 1 hour long matches with 25 year olds and under who are winners
midListWinnersUnderOneHour = data.query(
    '25 <= winner_age < 30 & minutes <= 60')

# Total num of matches won by >= 25 year old under 60 mins
# + 1 as programming starts at 0
midMatchesWonUnderOneHour = len(midListWinnersUnderOneHour.index) + 1
print(f'Middle aged matches won under 1 hour: {midMatchesWonUnderOneHour}')

# Get probability of winning a match under 2 hours
midProbabilityUnderOneHour = midMatchesWonUnderOneHour / totalMatchesWithMid
midProbabilityUnderOneHour = midProbabilityUnderOneHour * 100
midProbabilityUnderOneHour = round(midProbabilityUnderOneHour, 2)
print(
    f'Probability of a 25-30 year old winning a match under one hour: {midProbabilityUnderOneHour}%')


#
# +30 (30-inclusive) year old stats
#
print('')
print('+30 (30-inclusive) year old stats:')

# Get total number of matches played with a
# +30 year old (win or lose)
oldListLosersTotal = data.query('loser_age >= 30')
oldListWinnersTotal = data.query('winner_age >= 30')

# + 1 as programming starts at 0
totalMatchesWithOld = len(oldListLosersTotal.index) + \
    1 + len(oldListWinnersTotal.index) + 1
print(f'Total number of matches with a +30 year old: {totalMatchesWithOld}')

# take all of the under 2-hour long matches with +30 year olds who are winners
oldListWinnersUnderThreeHours = data.query('winner_age >= 30 & minutes<180')

# Total num of matches won by +30 year olds under 120 mins
# + 1 as programming starts at 0
oldMatchesWonUnderThreeHours = len(oldListWinnersUnderThreeHours.index) + 1
print(f'Older matches won under 3 hours: {oldMatchesWonUnderThreeHours}')

# Get probability of winning a match under 2 hours for +30 year olds
oldProbabilityUnderThreeHours = oldMatchesWonUnderThreeHours / totalMatchesWithMid
oldProbabilityUnderThreeHours = oldProbabilityUnderThreeHours * 100
oldProbabilityUnderThreeHours = round(oldProbabilityUnderThreeHours, 2)
print(
    f'Probability of a +30 year old winning a match under two hours: {oldProbabilityUnderThreeHours}%')

# take all of the under 2-hour long matches with +30 year olds who are winners
oldListWinnersUnderTwoHours = data.query('winner_age >= 30 & minutes<120')

# Total num of matches won by +30 year old under 120 mins
# + 1 as programming starts at 0
oldMatchesWonUnderTwoHours = len(oldListWinnersUnderTwoHours.index) + 1
print(f'Older aged matches won under 2 hours: {oldMatchesWonUnderTwoHours}')

# Get probability of winning a match under 2 hours
oldProbabilityUnderTwoHours = oldMatchesWonUnderTwoHours / totalMatchesWithOld
oldProbabilityUnderTwoHours = oldProbabilityUnderTwoHours * 100
oldProbabilityUnderTwoHours = round(oldProbabilityUnderTwoHours, 2)
print(
    f'Probability of a +30 year old winning a match under two hours: {oldProbabilityUnderTwoHours}%')

# Take all of the under 1 hour long matches with +30 year olds who are winners
oldListWinnersUnderOneHour = data.query('winner_age >= 30 & minutes <= 60')

# Total num of matches won by > 30 year old under 60 mins
# + 1 as programming starts at 0
oldMatchesWonUnderOneHour = len(oldListWinnersUnderOneHour.index) + 1
print(f'Older aged matches won under 1 hour: {oldMatchesWonUnderOneHour}')

# Get probability of winning a match under 2 hours
oldProbabilityUnderOneHour = oldMatchesWonUnderOneHour / totalMatchesWithOld
oldProbabilityUnderOneHour = oldProbabilityUnderOneHour * 100
oldProbabilityUnderOneHour = round(oldProbabilityUnderOneHour, 2)
print(
    f'Probability of a +30 year old winning a match under one hour: {oldProbabilityUnderOneHour}%')

# Probability of different ages winning a match
# Match Length        Probability
# Under 1 hour            n%
# Under 2 hours           n%
# Under 3 hours           n%

# create a df that has age range, probability
# y-axis - probability
# x-axis - time
probOfAgeGroups = pd.DataFrame({
    '25 years old or younger': [youthProbabilityUnderOneHour, youthProbabilityUnderTwoHours, youthProbabilityUnderThreeHours],
    '25-30 years old': [midProbabilityUnderOneHour, midProbabilityUnderTwoHours, midProbabilityUnderThreeHours],
    '+30 years old': [oldProbabilityUnderOneHour, oldProbabilityUnderTwoHours, oldProbabilityUnderThreeHours]},
    index=[60, 120, 180])
probOfAgeGroups.index.names = ['Times']

# Dislpay the dataframe of the probability of different age groups
print(probOfAgeGroups)

# Display the probabilties of the different age groups
for column in probOfAgeGroups:
    probOfAgeGroups[column].plot(
        title="Probability of age groups winning a match under a time constraint",
        legend=['25 years old and younger',
                '25-30 years old', '30 years old and older'],
        ylabel='Probability (in %)',
        xlabel='Times (in mins)',
        grid=True)
