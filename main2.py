import requests
import time
import pandas

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

# Convert game data jsons to csv
pandas.DataFrame.from_dict(min10.json()['allPlayers']).to_csv('min10.csv')
pandas.DataFrame.from_dict(min15.json()['allPlayers']).to_csv('min15.csv')
pandas.DataFrame.from_dict(min20.json()['allPlayers']).to_csv('min20.csv')