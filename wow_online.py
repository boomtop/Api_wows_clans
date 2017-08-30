from datetime import datetime
import requests
headers = {'X-Requested-With': 'XMLHttpRequest'}
outfile = open('Server.csv', 'w')
#EU = 'http://worldofwarships.eu/game-server-status/'
#NA http://worldofwarships.com/game-server-status/
#ASIA http://worldofwarships.asia/game-server-status/



Get = ['https://api.worldoftanks.asia/wgn/servers/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&game=wows', 'https://api.worldoftanks.eu/wgn/servers/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&game=wows',
       'https://api.worldoftanks.com/wgn/servers/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&game=wows', 'https://api.worldoftanks.ru/wgn/servers/info/?application_id=8c4db613cbca0ad5c601afcd44024acb&game=wows']
Region = ['Asia', 'EU', 'NA', 'RU']

test = []
for i in range(4):
    r = requests.get(Get[i])
    onlinePlayets = r.json()
    test.append(onlinePlayets['data']['wows'])
    outfile.write(test)
    print(test[i])

outfile.close()