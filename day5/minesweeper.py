
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
	# finalx = int(max(fromx, tox))
	# startx = int(min(fromx, tox))
	# finaly = int(max(fromy, toy))
	# starty = int(min(fromy, toy))

	if tox > fromx and toy < fromy:
		# Other more annoying calcs
	else:
		while startx <= finalx and starty <= finaly:
			grid[starty][startx] = 1 if grid[starty][startx] == 0 else grid[starty][startx] + 1
			if starty == finaly and startx == finalx:
				break
			if startx < finalx:
				startx += 1
			if starty < finaly:
				starty += 1
	return grid


fp = open('day5/inputfile', mode = 'r').readlines()

grid = [[int(0) for i in range(10)] for j in range(10)]

for line in fp:
	info = line.strip().split()
	da = info[0].split(',')
	a = info[2].split(',')
	grid = trace_line(grid, da[0], da[1], a[0], a[1])


for line in grid:
	print(line)
print(find_cross(grid))
