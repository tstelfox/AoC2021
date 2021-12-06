# from pathlib import Path
# import os
from array import *


def	solve_grids(grids):
	for grid in grids:
		print(grid)
		

fp = open('day4/inputfile', mode = 'r')

answers = fp.readline().split(',')
answers = list(map(str.strip, answers))

grid_data = fp.readlines()

# full_input = [map(str, x.split()) for x in grid_data]

grids = [grid_data[i: i + 6] for i in range(0, len(grid_data), 6)]
grids = [list(map(str.strip, grid)) for grid in grids]
# grids = []
# grid = []


# for line in grid_data:
# 	if i == 6:
# 		grids.append(grid)
# 		del(grid)
# 		i = 0
# 	grid.append(line.split())
# 	i += 1

print('grid 1 is:', grids[3])

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