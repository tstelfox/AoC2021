

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


# def fakefloodfill(floor):
#     dangerdangerhighvoltage = 0
#
#     for y, row in enumerate(floor):
#         for x, square in enumerate(row):
#             if lowest(floor, x, y):
#                 dangerdangerhighvoltage += square + 1
#     return dangerdangerhighvoltage


def fakefloodfill(floor):
    dangerdangerhighvoltage = 0
    for y, row in enumerate(floor):
        for x, square in enumerate(row):
            lowestest = True
            if (x > 0 and row[x-1] <= square) or (x < len(row) - 1 and row[x + 1] <= square):
                lowestest = False
            if (y > 0 and floor[y-1][x] <= square) or (y < len(floor) - 1 and floor[y + 1][x] <= square):
                lowestest = False
            if lowestest:
                dangerdangerhighvoltage += square + 1
    return dangerdangerhighvoltage


def dfs(grid):
    size = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            size = dfs(grid, y, x)
    return size

def dfs(grid, y, x):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid): return 0
    count = grid[y][x]

#     https://www.lavivienpost.com/depth-first-search-and-matrix/








def depth_first(floor):
    spelonche = []
    # size = 0
    visited = set()
    print(dfs(floor))





    return 'Do stuff'


if __name__ == '__main__':
    floor = []
    for line in open('inputfile').read().splitlines():
        floor.append([int(x)for x in line])
    # print(fakefloodfill(floor))
    print(depth_first(floor))
