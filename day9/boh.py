

# The following is my SHAMEFUL SIMPLE SMOOTH BRAIN
# def lowest(grid, x, y):
#     cell = grid[y][x]
#     if 0 < x < len(floor[0]) - 1 and 0 < y < len(floor) - 1:
#         if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
#             return True
#     if x == 0 and 0 < y < len(floor) - 1:
#         if grid[y][x + 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
#             return True
#     if x == len(floor[0]) - 1 and 0 < y < len(floor) - 1:
#         if grid[y][x - 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
#             return True
#     if y == 0 and 0 < x < len(floor[0]) - 1:
#         if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y + 1][x] > cell:
#             return True
#     if y == len(floor) - 1 and 0 < x < len(floor[0]) - 1:
#         if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y - 1][x] > cell:
#             return True
#     if x == 0 and y == 0:
#         if grid[y][x + 1] > cell and grid[y + 1][x] > cell:
#             return True
#     if y == len(floor) - 1 and x == len(floor[0]) - 1:
#         if grid[y][x - 1] > cell and grid[y - 1][x] > cell:
#             return True
#     if y == len(floor) - 1 and x == 0:
#         if grid[y - 1][x] > cell and grid[y][x + 1] > cell:
#             return True
#     if x == len(floor[0]) - 1 and y == 0:
#         if grid[y + 1][x] > cell and grid[y][x - 1] > cell:
#             return True
#     return False


def fakefloodfill(floor):
    fondali = []
    dangerdangerhighvoltage = 0
    for y, row in enumerate(floor):
        for x, square in enumerate(row):
            lowestest = True
            if (x > 0 and row[x-1] <= square) or (x < len(row) - 1 and row[x + 1] <= square):
                lowestest = False
            if (y > 0 and floor[y-1][x] <= square) or (y < len(floor) - 1 and floor[y + 1][x] <= square):
                lowestest = False
            if lowestest:
                fondali.append(x)
                fondali.append(y)
                dangerdangerhighvoltage += square + 1
    # return dangerdangerhighvoltage  # This is for exercise one
    return fondali


def idunno(grid, basin):
    size = 0
    for y, row in enumerate(grid):
        for x, square in enumerate(row):
            if grid[y][x] == 9:
                break
            # print(basin[1], basin[0])
            size += dfs(grid, basin[1], basin[0])
    return size

def dfs(grid, y, x):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 9 or grid[y][x] == 99:
        return 0
    count = 1
    grid[y][x] = 99  # visited
    i = y - 1
    while i < y + 1:
        j = x - 1
        while j < x + 1:
            count += dfs(grid, i, j)
            j += 1
        i += 1
    return count

#     https://www.lavivienpost.com/depth-first-search-and-matrix/

# Start from the lowest points in the grid.



if __name__ == '__main__':
    floor = []
    fondali = []
    for line in open('inputfile').read().splitlines():
        floor.append([int(x)for x in line])
    fondali = fakefloodfill(floor)
    # print(fondali)
    # for basin in fondali:
    i = 2
    while i <= len(fondali):
        # print(fondali[i-2:i])
        print(idunno(floor, fondali[i-2:i]))
        i += 2
    print(floor)
    # print(idunno(floor))
