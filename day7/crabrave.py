import statistics


def fuel_cost(crab_pos, pos):
    fuel = 0
    for crab in crab_pos:
        dist = abs(crab - pos)
        inc = 1
        for i in range(dist):
            fuel += inc
            inc += 1

    return fuel


def try_up(crab_pos, pos, previous):
    while 1:
        pos += 1
        fuel = fuel_cost(crab_pos, pos)
        if fuel > previous:
            return previous
        elif fuel > previous:
            previous = fuel
    return previous

def try_down(crab_pos, pos, previous):
    while 1:
        pos -= 1
        fuel = fuel_cost(crab_pos, pos)
        if fuel > previous:
            return previous
        elif fuel > previous:
            previous = fuel
    return previous

fp = open('inputfile', mode = 'r').readline()

crab_pos = list(map(int, fp.split(',')))

pos = int(statistics.mean(crab_pos))


previous = fuel_cost(crab_pos, pos)
fuelup = try_up(crab_pos, pos, previous)
fueldown = try_down(crab_pos, pos, previous)

fuel = min(fuelup, fueldown, previous)


print(fuel)
