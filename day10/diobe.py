
import statistics

def verify_closure(bracket, lastopened):
    if bracket == ')':
        if lastopened[len(lastopened) - 1] != 0:
            return 3
        lastopened.pop()
    if bracket == ']':
        if lastopened[len(lastopened) - 1] != 1:
            return 57
        lastopened.pop()
    if bracket == '}':
        if lastopened[len(lastopened) - 1] != 2:
            # print(lastopened)
            return 1197
        lastopened.pop()
    if bracket == '>':
        if lastopened[len(lastopened) - 1] != 3:
            return 25137
        lastopened.pop()
    return 0

def check_corrupt(input):
    # types = [0] * 4
    # print(types)
    lastopened = []

    for bracket in input:
        # print(lastopened)
        if bracket == '(':
            lastopened.append(0)
            # types[0] += 1
        if bracket == '[':
            lastopened.append(1)
            # types[1] += 1
        if bracket == '{':
            lastopened.append(2)
            # types[2] += 1
        if bracket == '<':
            lastopened.append(3)
            # types[3] += 1
        # if bracket == ')':
        #     types[0] -= 1
        # if bracket == ']':
        #     types[1] -= 1
        # if bracket == '}':
        #     types[2] -= 1
        # if bracket == '>':
        #     types[3] -= 1
        if ret := verify_closure(bracket, lastopened):
            return ret
    return 0

def check_rest(input):
    types = [0] * 4
    lastopened = []
    score = 0

    for bracket in input:
        if bracket == '(':
            lastopened.append(0)
            types[0] += 1
        if bracket == '[':
            lastopened.append(1)
            types[1] += 1
        if bracket == '{':
            lastopened.append(2)
            types[2] += 1
        if bracket == '<':
            lastopened.append(3)
            types[3] += 1
        if bracket == ')':
            types[0] -= 1
            lastopened.pop()
        if bracket == ']':
            types[1] -= 1
            lastopened.pop()
        if bracket == '}':
            types[2] -= 1
            lastopened.pop()
        if bracket == '>':
            types[3] -= 1
            lastopened.pop()
    for bracket in lastopened:
        print(score)
        score *= 5
        if lastopened[len(lastopened) - 1] == 0:
            score += 1
        elif lastopened[len(lastopened) - 1] == 1:
            score += 2
        elif lastopened[len(lastopened) - 1] == 2:
            score += 3
        elif lastopened[len(lastopened) - 1] == 3:
            score += 4
        lastopened.pop()
        # if ret := verify_closure(bracket, lastopened):
        #     return ret
    return score


if __name__ == '__main__':
    lines = open("testfile.txt").read().splitlines()

incomplete = []
point = 0
for line in lines:
    bracket = 0
    if bracket := check_corrupt(line):
        point += bracket
    else:
        incomplete.append(line)
# print(point)
# print(incomplete)
points2 = []
for line in incomplete:
    points2.append(check_rest(line))
# print(points2)
print(statistics.median(points2))