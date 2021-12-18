
import math
# The following is my SHAMEFUL SIMPLE SMOOTH BRAIN
# vroom vroom

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
    return fondali


def idunno(grid, fondali):
    size = 0
    y = fondali[1]
    x = fondali[0]
    size = dfs(grid, y, x)
    return size

def dfs(grid, y, x):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid) or grid[y][x] == 9 or grid[y][x] == -1:
        return 0
    grid[y][x] = -1
    count = 1

    # WHAT WAS THIS SHAMEFUL SHIT ABOUT ??? STOOPID STOOPID STOOPID
    # for row in range(y - 1, y + 1):
    #     for item in range(x - 1, x + 1):
            # if grid[y][x] != 9:
    count += dfs(grid, y - 1, x)
    count += dfs(grid, y + 1, x)
    count += dfs(grid, y, x - 1)
    count += dfs(grid, y, x + 1)
    return count


if __name__ == '__main__':
    floor = []
    fondali = []
    basins = []
    for line in open('inputfile').read().splitlines():
        floor.append([int(x)for x in line])

    fondali = fakefloodfill(floor)
    i = 2
    while i <= len(fondali):
        basins.append(idunno(floor, fondali[i-2:i]))
        i += 2
    basins = sorted(basins, reverse=True)[:3]
    print(math.prod(basins))

