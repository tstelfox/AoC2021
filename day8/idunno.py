lines = open('inputfile').read().splitlines()

cnt_easy = 0
lines = [line.split('|') for line in lines]

clocks = []

for line in lines:
    clocks.append(line[1])

for clock in clocks:
    count_now = clock.split()
    for items in count_now:
        if len(items) >= 2 and len(items) <= 4 or len(items) == 7:
            cnt_easy += 1

print(cnt_easy)