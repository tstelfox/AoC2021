fp = open('inputfile', mode = 'r').readline()

first_fish = list(map(int, (fp.split(','))))

fishes = []
fishes = [0 for i in range(9)]
for fish in first_fish:
    fishes[fish] += 1
for cycle in range(256):
    fishes[7] += fishes[0]
    newborn = fishes[0]
    fishes.append(newborn)
    fishes.pop(0)



print(sum(fishes))