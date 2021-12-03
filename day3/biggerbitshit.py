
from itertools import combinations

lines = open('inputfile', mode = 'r').read().split()

bitlist = list('000000000000')

cnt_one = 0
cnt_zero = 0
# check_one = 0
# check_zero = 0
filtered = []

def	first_filter(to_filter, lines, filtered, i):
	if to_filter == '1':
		for line in lines:
			if line[i] == '1':
				filtered.append(line[i])
	elif to_filter == '0':
		for line in lines:
			if line[i] == '0':
				filtered.append(line[i])

def filter_bits(to_filter, filtered, i):
	if to_filter == '1':
		for line in filtered:
			if line[i] == '1':
				filtered.append(line[i])
	elif to_filter == '0':
		for line in filtered:
			if line[i] == '0':
				filtered.append(line[i])


for line in lines:
	if line[0] == '1':
		cnt_one += 1
	elif line[0] == '0':
		cnt_zero += 1
first_filter(cnt_one, lines, filtered, i) if cnt_one >= cnt_zero else first_filter(cnt_zero, lines, filtered, i)
i = 1
cnt_one = 0
cnt_zero = 0
while len(filtered) not 1: // Actually range needs to be until there is only one number left
	i = 1
	for filtered in range(filtered):
		if filtered[i] == '1'
			cnt_one += 1
		elif filtered[i] == '0'
			cnt_zero += 1
	i += 1
	filter_bits(cnt_one ,filtered, i) if cnt_one >= cnt_zero else filter_bits(cnt_zero ,filtered, i)
	cnt_zero = 0
	cnt_one = 0

oxystr = ''.join(map(str, filtered))

oxyint = int(oxystr, 2)

print(oxyint)
	
	# bitlist[i] = '1' if cnt_one > cnt_zero else '0'

# combinations(range(2), 4)

# combos = combinations(range(2), 4)

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



