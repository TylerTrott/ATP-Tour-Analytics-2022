# ATP-Tour-Analytics-2022
Here is my personal project of data analytics from the ATP tour 2022 season

ATP (Association of Tennis Professionals)
Dataset of matches, tournaments and players of 2022

The following dataset includes all information of the ATP Tour of 2022. The dataseet includes fields such as; 

Tournament information:
tournament ID, tournament name, tournament location, players who played in that tournament, tournament court surface,  what level the tournament is (levels range from 250 - 1000, 2000 for Grand Slams), match durations (times)

Player information:
Names, rankings, country of birth, age, tournaments won

This dataset can be found on a GitHub repository titled, 'Awesome Public Datasets'. 
The repository can be found [here](https://github.com/awesomedata/awesome-public-datasets#esports)
The ATP dataset can be found [here](https://github.com/JeffSackmann/tennis_atp)

Potential interesting questions:
Using data that already exists:
  - [x] What is the probability of different age ranges winning a match under 1,2, and 3 hour(s)?
    - [ ] What is this probability in different level tournaments? 250, 500, 1000, 2000?
  - [ ] What is the average number of rank changes within the top 100 ranked players?
  - [ ] What is the probability of the top 10 ranked players to win a tournament?
  - [ ] What is the average match duration in a tournament that is at level; 250, 500, 1000, 2000?

Predictions:
  - [ ] Based on which players won tournaments this year, what is the likelihood that these players will win the tournaments again next year?
  - [ ] Based on the number of wins on a specific court, which players are likely to win a tournament (with the same court type) next year?

Update (Winter Semester 2023):
Have now included R code. 

This code looks into nationalities of players and their success in tournaments. There is a geographical map of the world that lays out the distribution of players who have won and lost matches in tournaments. 

Another thing I have added within this R code is an insight about the age of players and court surface type. It is a box plot that shows the age distribution depending on whether the court surface is clay, grass or hard.

Lastly, the R code includes a graph that displays a relationship between age and the duration of a match. The insight includes both the winner and loser of the match.