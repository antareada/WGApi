import json
import struct

replay = open("20140523_1828_usa-T34_hvy_10_hills.wotreplay", "rb")
# Эти 8 байтов ты тупо пропускаешь

header = replay.read( 8 )
if header[4] == 1: # статистики нет
	length = replay.read(4)
	length = struct.unpack('i', length)
	data = replay.read(length[0])

	d = json.loads(data.decode("ascii"))

	print(d)

elif header[4] == 2: # статистика есть
	length = replay.read(4)
	length = struct.unpack('i', length)
	data = replay.read(length[0])

	d = json.loads(data.decode("ascii"))

	print(d)

	length = replay.read(4)
	length = struct.unpack('i', length)

	data = replay.read(length[0])

	print(length)
	f = open('data.txt', 'a')
	f.write(str(data))

	l = json.loads(data.decode("ascii"))

	print(len(l))

else: # все плохо
	print('Error')