fp = open('inputfile', mode = 'r')

depth = 0
position = 0
aim = 0

def move(value):
	return int(value)


row = fp.readlines()

for line in row:
	info = line.split()
	command = info[0]
	# print(info[0])
	x = int(info[1])
	if command == 'forward':
		position += move(x)
		depth += x * aim
	if command == 'up':
		aim -= move(x)
	if command == 'down':
		aim += move(x)

fp.close()
print('Depth', depth, 'position', position, 'and multiplied', depth * position)
