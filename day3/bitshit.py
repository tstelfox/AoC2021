lines = open('inputfile', mode = 'r').read().split()

bitstr = list('000000000000')

cnt_one = 0
cnt_zero = 0

for i in range(12):
	for line in lines:
		if line[i] == '1':
			cnt_one += 1
		elif line[i] == '0':
			cnt_zero += 1
	bitstr[i] = '1' if cnt_one > cnt_zero else '0'
	cnt_one = 0
	cnt_zero = 0

gamma = bitstr

# epsilon = gamma
epsilon = list('000000000000')
for i in range(12):
	if gamma[i] == '1':
		epsilon[i] = '0'
	else:
		epsilon[i] = '1'
gammastr = ''.join(map(str, gamma))
epsilonstr = ''.join(map(str, epsilon))

print('gamma is ', gammastr, 'epsilon is ', epsilonstr)


gammaint = int(gammastr, 2)
epsilonint = int(epsilonstr, 2)

# gammaout = 0
# for bit in gamma:
# 	gammaout = (gamma << 1) | bit

# epsilonout = 0
# for bit in epsilon:
# 	epsilonout = (epsilon << 1) | bit

print('gamma as int ', gammaint, 'epsilon as int ', epsilonint)

print('Multiplied they are ', gammaint * epsilonint)
