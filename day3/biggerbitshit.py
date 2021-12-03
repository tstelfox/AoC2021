
from itertools import combinations

lines = open('inputfile', mode = 'r').read().split()

bitlist = list('000000000000')

cnt_one = 0
cnt_zero = 0


for line in lines:
	if line[0] == '1':
		cnt_one += 1
	elif line[0] == '0':
		cnt_zero += 1
bitlist[0] = '1' if cnt_one > cnt_zero else '0'

# combinations(range(2), 4)

combos = combinations(range(2), 4)

# print(combos[0])

# ------
# gamma = bitlist

# # epsilon = gamma
# epsilon = list('000000000000')
# for i in range(12):
# 	if gamma[i] == '1':
# 		epsilon[i] = '0'
# 	else:
# 		epsilon[i] = '1'
# gammastr = ''.join(map(str, gamma))
# epsilonstr = ''.join(map(str, epsilon))

# print('gamma is ', gammastr, 'epsilon is ', epsilonstr)



