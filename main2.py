import requests, time

# Timer loop prep
# Open files for specific times
min10 = open("min10.json", "w")
min15 = open("min15.json", "w")
min20 = open("min20.json", "w")

startTime = time.time()
currentTime = 0

# Toggle variables for when loop meets if conditions
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
    if currentTime == 60*10 and not collected10:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min10.write(currentMatch.text)
        collected10 = True
        print("10 mins")

    # Match data at 15 mins
    if currentTime == 60*15 and not collected15:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min15.write(currentMatch.text)
        collected15 = True
        print("15 mins")

    # Match data at 20 mins
    if currentTime == 60*20 and not collected20:
        currentMatch = requests.get('https://127.0.0.1:2999/liveclientdata/allgamedata', verify='riotgames.pem')
        min20.write(currentMatch.text)
        collected20 = True
        print("20 mins")
        break

# Close the files
min10.close()
min15.close()
min20.close()
