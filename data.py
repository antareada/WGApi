import json
import struct
import requests

s = requests.Session()

application_id = '01832d316a2655bc17523d78862950fc'

lvl = [0, 2, 3, 5, 8, 12, 18, 27, 40, 60, 100]
types = {'mediumTank': 1, 'heavyTank': 1.2, 'AT-SPG': 1.2, 'SPG': 1, 'lightTank': 1}
d = {'Object252': 'IS-6'}
r = s.get("https://api.worldoftanks.ru/wot/encyclopedia/tanks/?application_id=demo&fields=name,type,level").json()


def team(team_number, data):
	return list(d['vehicleType'].split(':')[1] for d in data['vehicles'].values() if d['team'] == team_number)

def statical_data():
	length = replay.read(4)
	length = struct.unpack('i', length)
	data = replay.read(length[0])

	d = json.loads(data.decode("ascii"))
	f = open('data1.txt', 'w')
	json.dump(d, f, indent=2)
	first_team = team(1, d)
	second_team = team(2, d)

	print(first_team)
	print(second_team)

	tank_dict = tanks(r)
	print("Первая команда:")
	print(balance(first_team, tank_dict))
	print("Вторая команда:")
	print(balance(second_team, tank_dict))


def tanks(tanks):
	
	tanks = {item['name'].split(':')[1]: item for item in r['data'].values()}
	
	for i in tanks.values():
		i['value'] = lvl[i['level']] * types[i['type']]
	f = open('data3.txt', 'w')
	json.dump(tanks, f, indent=2)
	return tanks

def balance(team, tanks):
	a = 0
	for i in team:
		print(d.get(i, i), tanks[d.get(i, i)]['value'])
		a += tanks[d.get(i, i)]['value']
	return a


replay = open("20140524_2304_china-Ch23_112_34_redshire.wotreplay", "rb")
# Эти 8 байтов ты тупо пропускаешь

header = replay.read( 8 )
if header[4] == 1: # статистики нет
	statical_data()

elif header[4] == 2: # статистика есть
	statical_data()

	length = replay.read(4)
	length = struct.unpack('i', length)

	data = replay.read(length[0])
	l = json.loads(data.decode("ascii"))
	f = open('data2.txt', 'w')
	json.dump(l, f, indent=2)

else: # все плохо
	print('Error')