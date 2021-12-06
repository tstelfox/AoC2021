# from pathlib import Path
# import os
from array import *

def	calculate_points(grid, winner):
	points = 0
	for row in grid:
		for i in row:
			if i != 'x':
				points += int(i)
	print(int(winner) * points)
	return True

def	check_winner(grids, winner):
	g = 0
	bingo = 0
	for grid in grids:
		h = 0
		i = 0
		while i in range(len(grid)):
			while h in range(len(grid)):
				if grid[h][i] == 'x':
					bingo += 1
				if bingo == 5:
					return calculate_points(grid, winner)
				h += 1
			i += 1
			h = 0
			bingo = 0
		i = 0
		while h in range(len(grid)):
			while i in range(len(grid)):
				if grid[h][i] == 'x':
					bingo += 1
				if bingo == 5:
					return calculate_points(grid, winner)
				i += 1
			h += 1
			i = 0
			bingo = 0
		bingo = 0
		g += 1

def	solve_grids(grids, answers):
	for num in answers:
		g = 0
		for grid in grids:
			for i in range(len(grid)):
				for k in range(5):
					if num == grids[g][k][i]:
						winner = num
						grids[g][k][i] = 'x'
			g += 1
		if check_winner(grids, winner) is True:
			return
		
		

fp = open('day4/inputfile', mode = 'r')

answers = fp.readline().split(',')
answers = list(map(str.strip, answers))

grid_data = fp.readlines()

# The following three lines caused me grief because I was wrapping my head around how lists work in python
grids = [grid_data[i: i + 6] for i in range(0, len(grid_data), 6)]
grids = [list(map(str.strip, grid)) for grid in grids]

grids = [line.split() for grid in grids for line in grid]

grid = []
realgrids = []
i = 0
for row in grids:
	if i != 0:
		grid.append(row)
	i += 1
	if i == 6:
		i = 0
		realgrids.append(grid)
		grid = []

solve_grids(realgrids, answers)

