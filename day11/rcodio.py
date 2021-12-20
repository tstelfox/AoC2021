def floodfill(octo_grid, x, y):
    if x < 0 or y < 0 or y > len(octo_grid) - 1 or x > len(octo_grid[0]) - 1 or octo_grid[y][x] == -1:
        return 0
    flashes = 0
    octo_grid[y][x] += 1
    if octo_grid[y][x] == 10:
        flashes = 1
        octo_grid[y][x] = -1
        for i in range(x-1, x+2):
            for k in range(y-1, y+2):
                flashes += floodfill(octo_grid, i, k)
    return flashes


def increment_octos(octo_grid):
    flashes = 0
    for y, row in enumerate(octo_grid):
        for x, octo in enumerate(row):
            flashes += floodfill(octo_grid, x, y)

    for y, row in enumerate(octo_grid):
            for x, octo in enumerate(row):
                if octo == -1:
                    octo_grid[y][x] = 0
    return flashes



if __name__ == '__main__':
    grid = []
    flashes = 0
    for line in open('inputfile.txt').read().splitlines():
        grid.append([int(x) for x in line])
    for i in range(100):
        flashes += increment_octos(grid)
    for row in grid:
        print(row)
    print(flashes)