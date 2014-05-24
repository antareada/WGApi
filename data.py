import json
import struct

replay = open("20140523_1840_usa-T34_hvy_38_mannerheim_line.wotreplay", "rb")
# Эти 8 байтов ты тупо пропускаешь

replay.read(8)

length = replay.read(4)
length = struct.unpack('i', length)
data = replay.read(length[0])

d = json.loads(data.decode("ascii"))

print(d.keys())

length = replay.read(4)
length = struct.unpack('i', length)

data = replay.read(length[0])

print(length)
f = open('data.txt', 'a')
f.write(str(data))

l = json.loads(data.decode("ascii"))

print(len(l))