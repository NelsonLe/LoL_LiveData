import requests
import time
from riotwatcher import LolWatcher

# Set up watcher
key = 'Your Riot API Key here'
watcher = LolWatcher(key)
region = 'na1'

# In-game player summoner name
summonerName = 'Desired summoner name'

# Get summoner id
summonerId = watcher.summoner.by_name(region, summonerName)['id']

# Get match start time
startTime = watcher.spectator.by_summoner(region, summonerId)['gameStartTime']/1000

# Timer loop prep
# Open files for specific times
min1 = open("min1.txt", "w")
min10 = open("min10.txt", "w")
min15 = open("min15.txt", "w")
min20 = open("min20.txt", "w")

# Init vars
gameLength = 0

# Timer loop
while True:
    deltaTime = time.time() - startTime

    # Reduces number of requests to Riot to about 4/sec
    if deltaTime >= .25:
        gameLength = watcher.spectator.by_summoner(region, summonerId)['gameLength']
        startTime += .25

    # Match data at 1 mins
    if gameLength == 60:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min1.write(currentMatch.text)
        print("1 mins")

    # Match data at 10 mins
    if gameLength == 600:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min10.write(currentMatch.text)
        print("10 mins")

    # Match data at 15 mins
    if gameLength == 900:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min15.write(currentMatch.text)
        print("15 mins")

    # Match data at 20 mins
    if gameLength == 1200:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min20.write(currentMatch.text)
        print("20 mins")
        break

# Close the files
min1.close()
min10.close()
min15.close()
min20.close()
