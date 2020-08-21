import requests
import time

# Timer loop prep
# Open files for specific times
min10 = open("min10.json", "w")
min15 = open("min15.json", "w")
min20 = open("min20.json", "w")
startTime = time.time()

# Init
currentTime = 0

# Timer loop
while True:
    # Request from Riot 2/sec
    if time.time() - startTime >= .5:
        startTime += .5
        currentTime = int(requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem').json()['gameData']['gameTime'])

    # Match data at 10 mins
    if currentTime == 60*10:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min10.write(currentMatch.text)
        print("10 mins")

    # Match data at 15 mins
    if currentTime == 60*15:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min15.write(currentMatch.text)
        print("15 mins")

    # Match data at 20 mins
    if currentTime == 60*20:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min20.write(currentMatch.text)
        print("20 mins")
        break

# Close the files
min10.close()
min15.close()
min20.close()
