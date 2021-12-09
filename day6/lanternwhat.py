fp = open('inputfile', mode = 'r').readline()

fishies = list(map(int, (fp.split(','))))


for i in range(256):
    for fish in range(len(fishies)):
        if fishies[fish] == 0:
            fishies.append(8)
            fishies[fish] = 7
        fishies[fish] -= 1

print(len(fishies))