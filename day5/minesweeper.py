
# def	horivertal(grid, line, i):
# 	horizontal = True
	# vertical = True
	# for height in range(len(grid)):
	# 	for length in range(len(line)):
	# 		if line[length] != 'T' and line[length] != '1':
	# 			horizontal = False
	# 			break;
	# 	if grid[height][i] != 'T' and grid[height][i] != '1':
	# 		vertical = False
	# 		break;
	# if horizontal and vertical is False:
	# 	return False
	# else: 
	# 	return True
		

def	find_cross(grid):
	cnt_overlap = 0
	for line in grid:
		for i in line:
			if (i > 1):
				cnt_overlap += 1					
	return cnt_overlap

def	trace_line(grid, fromx, fromy, tox, toy):
	
	fromx = int(fromx)
	fromy = int(fromy)
	tox = int(tox)
	toy = int(toy)
	

	if fromx == tox:
		finaly = int(max(fromy, toy))
		starty = int(min(fromy, toy))
		while starty <= finaly:
			grid[starty][int(fromx)] += 1
			if starty <= finaly:
				starty += 1
		return grid
	elif fromy == toy:
		finalx = int(max(fromx, tox))
		startx = int(min(fromx, tox))
		while startx <= finalx:
			grid[int(fromy)][startx] += 1
			if startx <= finalx:
				startx += 1
		return grid
	elif fromx != tox and fromy != toy:
		while True:
			grid[fromy][fromx] += 1
			if fromx == tox and fromy == toy:
				break
			fromx += 1 if tox > fromx else -1
			fromy += 1 if toy > fromy else -1
	return grid


fp = open('day5/inputfile', mode = 'r').readlines()

grid = [[int(0) for i in range(1000)] for j in range(1000)]

for line in fp:
	info = line.strip().split()
	da = info[0].split(',')
	a = info[2].split(',')
	grid = trace_line(grid, da[0], da[1], a[0], a[1])


print(find_cross(grid))
