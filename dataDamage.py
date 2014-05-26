import json
import struct


def team(team_number, data):
	return list(d['vehicleType'].split(':')[1] for d in data['vehicles'].values() if d['team'] == team_number)

def statical_data():
	length = replay.read(4)
	length = struct.unpack('i', length)
	data = replay.read(length[0])

	d = json.loads(data.decode("ascii"))
	f = open('data1.txt', 'w')
	json.dump(d, f, indent=2)
	if d['battleType'] == 1:
		print("Тип боя: Стандартный.")
	else:
		print('Тип боя не является Стандартным. Дальнейшие расчеты не имеют смысла.')


replay = open("20140527_0151_germany-Ltraktor_04_himmelsdorf.wotreplay", "rb")
# Эти 8 байтов ты тупо пропускаешь

header = replay.read( 8 )
if header[4] == 1: # статистики нет
	print('Игрок не дождался окончания боя. Данных не будет. :(')

elif header[4] == 2: # статистика есть
	statical_data()

	length = replay.read(4)
	length = struct.unpack('i', length)

	data = replay.read(length[0])
	l = json.loads(data.decode("ascii"))
	f = open('data2.txt', 'w')
	json.dump(l, f, indent=2)
	damage_first = list((i['health'] + i['damageReceived']) for i in l[0]['vehicles'].values() if i['team'] == 1)
	damage_second = list((i['health'] + i['damageReceived']) for i in l[0]['vehicles'].values() if i['team'] == 2)
	
	sum_damage_first = sum(damage_first)
	print('Суммарная прочность первой команды:')
	print(sum_damage_first)
	sum_damage_second = sum(damage_second)
	print('Суммарная прочность второй команды:')
	print(sum_damage_second)
	damage_tuple = l[0]['vehicles'].items()
	damage_dealt = []
	for key, d in damage_tuple:
		damage_dealt.append((d['damageDealt'], key))

	max_damage, user_max_damage_id = max(damage_dealt)

	user_name = l[1][user_max_damage_id]['name']
	print('Ник игрока, который претендует на "Основной калибр":')
	print(user_name)
	print('Урон, который нанес игрок (для получения награды должен быть не меньше 1000):')
	print(max_damage)
	print('Урон по союзникам, который нанес игрок:')
	print(l[0]['vehicles'][user_max_damage_id]['tdamageDealt'])

	if l[1][user_max_damage_id]['team'] == 1:
		print('Игрок находится в команде 1.')
		print('Процент от суммарной прочности противников:')
		print(max_damage / sum_damage_second * 100)
	elif l[1][user_max_damage_id]['team'] == 2:
		print('Игрок находится в команде 2.')
		print('Процент от суммарной прочности противников:')
		print(max_damage / sum_damage_first * 100)


else: # все плохо
	print('Error')