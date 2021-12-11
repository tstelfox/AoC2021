
def lowest(grid, x, y):
    cell = grid[y][x]
    if 0 < x < len(floor[0]) - 1 and 0 < y < len(floor) - 1:
        # print(x, y)
        if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
            return True
    if x == 0 and 0 < y < len(floor) - 1:
        if grid[y][x + 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
            return True
    if x == len(floor[0]) - 1 and 0 < y < len(floor) - 1:
        if grid[y][x - 1] > cell and grid[y + 1][x] > cell and grid[y - 1][x] > cell:
            return True
    if y == 0 and 0 < x < len(floor[0]) - 1:
        if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y + 1][x] > cell:
            return True
    if y == len(floor) - 1 and 0 < x < len(floor[0]) - 1:
        if grid[y][x + 1] > cell and grid[y][x - 1] > cell and grid[y - 1][x] > cell:
            return True
    if x == 0 and y == 0:
        if grid[y][x + 1] > cell and grid[y + 1][x] > cell:
            return True
    if y == len(floor) - 1 and x == len(floor[0]) - 1:
        if grid[y][x - 1] > cell and grid[y - 1][x] > cell:
            return True
    if y == len(floor) - 1 and x == 0:
        if grid[y - 1][x] > cell and grid[y][x + 1] > cell:
            return True
    if x == len(floor[0]) - 1 and y == 0:
        if grid[y + 1][x] > cell and grid[y][x - 1] > cell:
            return True
    return False


def fakefloodfill(floor, x, y):
    dangerdangerhighvoltage = 0


    for y in range(len(floor)):
        for x in range(len(floor[0])):
            if lowest(floor, x, y):
                print(floor[y][x], x, y)
                dangerdangerhighvoltage += floor[y][x] + 1
    #         if 0 <= y < len(floor) and 0 <= x < len(floor[0]):
    #             cell = floor[y][x]
    #         if x < len(floor[0]) - 1:
    #             if floor[y][x + 1] < cell:
    #                 x += 1
    #         if x > 0:
    #             if floor[y][x - 1] < cell:
    #                 x -= 1
    #         if y > 0:
    #             if floor[y - 1][x] < cell:
    #                 y -= 1
    #         if y < len(floor) - 1:
    #             if floor[y + 1][x] < cell:
    #                 y +=
    return dangerdangerhighvoltage


if __name__ == '__main__':
    floor = []
    for line in open('inputfile').read().splitlines():
        floor.append([int(x)for x in line])
    print(fakefloodfill(floor, 0, 0))

# print(floor)