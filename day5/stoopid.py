def	find_cross(grid):
	cnt_overlap = 0
	for line in grid:
		for i in line:
			if (i > 1):
				cnt_overlap += 1					
	return cnt_overlap

def	trace_line(grid, fromx, fromy, tox, toy):

	# finaly = int(max(fromy, toy))
	# starty = int(min(fromy, toy))
	# finalx = int(min(fromx, tox))
	# startx = int(max(fromx, tox))


	fromx = int(fromx)
	fromy = int(fromy)
	tox = int(tox)
	toy = int(toy)
	if fromx == tox:
		finaly = int(max(fromy, toy))
		starty = int(min(fromy, toy))
		while starty <= finaly:
			grid[starty][int(fromx)] = 1 if grid[starty][int(fromx)] == 0 else grid[starty][int(fromx)] + 1
			# print(starty, finaly)
			if starty <= finaly:
				starty += 1
		# print('Last case ', starty, finaly)
		return grid
	elif fromy == toy:
		finalx = int(max(fromx, tox))
		startx = int(min(fromx, tox))
		while startx <= finalx:
			grid[int(fromy)][startx] = 1 if grid[int(fromy)][startx] == 0 else grid[int(fromy)][startx] + 1
			if startx <= finalx:
				startx += 1
		return grid

	return grid


fp = open('day5/inputfile', mode = 'r').readlines()

grid = [[int(0) for i in range(1000)] for j in range(1000)]

for line in fp:
	info = line.strip().split()
	da = info[0].split(',')
	a = info[2].split(',')
	grid = trace_line(grid, da[0], da[1], a[0], a[1])

# for line in grid:
# 	print(line)

print(find_cross(grid))
