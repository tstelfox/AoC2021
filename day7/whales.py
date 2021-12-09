import statistics

fp = open('inputfile', mode = 'r').readline()

crab_pos = list(map(int, fp.split(',')))

pos = int(statistics.median(crab_pos))

fuel = 0
for crab in crab_pos:
    fuel += abs(crab - pos)
print(fuel)
