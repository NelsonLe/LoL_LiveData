import requests
import time
import pandas
import json

# Timer loop prep
startTime = time.time()
currentTime = 0  # Init
# Toggles when data is collected so it does not collect more than once
collected10 = False
collected15 = False
collected20 = False

# Timer loop
while True:
    # Request 2/sec
    if time.time() - startTime >= .5:
        startTime += .5
        currentTime = int(requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem').json()['gameData']['gameTime'])

    # Match data at 10 mins
    if not collected10 and currentTime == 60*10:
        min10 = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        collected10 = True
        print("10 mins")

    # Match data at 15 mins
    if not collected15 and currentTime == 60*15:
        min15 = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        collected15 = True
        print("15 mins")

    # Match data at 20 mins
    if not collected20 and currentTime == 60*20:
        min20 = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        collected20 = True
        print("20 mins")
        break

# Convert all players' game data from dictionary to dataframe
min10Data = pandas.DataFrame.from_dict(min10.json()['allPlayers'])
min15Data = pandas.DataFrame.from_dict(min15.json()['allPlayers'])
min20Data = pandas.DataFrame.from_dict(min20.json()['allPlayers'])

# Subset the data
min10Data = min10Data[['championName', 'level', 'position', 'summonerName']]
min15Data = min15Data[['championName', 'level', 'position', 'summonerName']]
min20Data = min20Data[['championName', 'level', 'position', 'summonerName']]

# Convert all players' scores from dict to dataframe
min10DataScores = pandas.DataFrame.from_dict(min10.json()['allPlayers'][0]['scores'])
for i in range(1, 10):
    temp = pandas.DataFrame(min10.json()['allPlayers'][i]['scores'], index=[i])
    min10DataScores = min10DataScores.append(temp)

min15DataScores = pandas.DataFrame.from_dict(min15.json()['allPlayers'][0]['scores'])
for i in range(1, 10):
    temp = pandas.DataFrame(min15.json()['allPlayers'][i]['scores'], index=[i])
    min15DataScores = min15DataScores.append(temp)

min20DataScores = pandas.DataFrame.from_dict(min20.json()['allPlayers'][0]['scores'])
for i in range(1, 10):
    temp = pandas.DataFrame(min20.json()['allPlayers'][i]['scores'], index=[i])
    min20DataScores = min20DataScores.append(temp)

# Merge data frames
min10Data = min10Data.join(min10DataScores)
min15Data = min15Data.join(min15DataScores)
min20Data = min20Data.join(min20DataScores)

# Convert game data jsons to csv
min10Data.to_csv('min10.csv')
min15Data.to_csv('min15.csv')
min20Data.to_csv('min20.csv')
