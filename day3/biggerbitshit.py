
def	find_common(lines, criterion, i):
	cnt_one = 0
	cnt_zero = 0
	for line in lines:
		if line[i] == '1':
			cnt_one += 1
		if line[i] == '0':
			cnt_zero += 1
	if (criterion == 'more'):
		return '1' if cnt_one >= cnt_zero else '0'
	elif (criterion == 'less'):
		return '0' if cnt_one >= cnt_zero else '1'


lines = open('inputfile', mode = 'r').read().split()
l2 = lines

for i in range(len(lines[0])):
	b = find_common(lines, 'more', i)
	lines = [l for l in lines if l[i] == b]
	if len(lines) == 1:
		oxygen = (int(lines[0], 2))
	# print('lines is ', lines, 'and i is ', i)

for i in range(len(l2[0])):
	b = find_common(l2, 'less', i)
	l2 = [l for l in l2 if l[i] == b]
	if len(l2) == 1:
		c02 =(int(l2[0], 2))
	# print('l2 is ', l2, 'and i is ', i)


print(oxygen * c02)