# from pathlib import Path
# import os
from array import *


def	solve_grids(grids, answers):
	
	# for i in range(len(answers)):
	# 	num = answers[i]
	# 	g = 0
	# 	for grid in grids:

	
	
	for num in answers:
		g = 0
		for grid in grids:
			for i in range(len(grid)):
				if i == 0:
					i += 1
				for k in range(6):
					print(grids[g][k])
					# Getting there?
					# if num == grid[g][i][k]:
						# print("Pino sei grande")
						# print(grid[i][k])
						# print(i, k)
						# grids[g][i][k] = 'x'
			g += 1
	# print(grids)
		
		

fp = open('day4/inputfile', mode = 'r')

answers = fp.readline().split(',')
answers = list(map(str.strip, answers))

grid_data = fp.readlines()

grids = [grid_data[i: i + 6] for i in range(0, len(grid_data), 6)]
grids = [list(map(str.strip, grid)) for grid in grids]

grids = [line.split() for grid in grids for line in grid]
	# for line in gr()id:
	# 	line.split



solve_grids(grids, answers)

# print(grids)

# for line in grid_data:
# 	if i == 6:
# 		grids.append(grid)
# 		del(grid)
# 		i = 0
# 	grid.append(line.split())
# 	i += 1

print(grids[0])

# print(grids)


# grids = []
# grid = []
# ln_cnt = 0
# for line in grid_data:
# 	if line == 6:
# 		grid.append(line)
# 		ln_cnt += 1
# 		if ln_cnt == 5:
# 			grids.append(grid)
# 			ln_cnt = 0
# 			del(grid)


# print(grids)

# print(answers)