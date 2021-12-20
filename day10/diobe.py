
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
            return 1197
        lastopened.pop()
    if bracket == '>':
        if lastopened[len(lastopened) - 1] != 3:
            return 25137
        lastopened.pop()
    return 0

def check_corrupt(input):
    lastopened = []

    for bracket in input:
        if bracket == '(':
            lastopened.append(0)
        if bracket == '[':
            lastopened.append(1)
        if bracket == '{':
            lastopened.append(2)
        if bracket == '<':
            lastopened.append(3)
        if ret := verify_closure(bracket, lastopened):
            return ret
    return 0

def complete_line(lastopened):
    # Check the last bracket opened and score according to closing bracket
    score = 0
    for i in range(len(lastopened)):
        score *= 5
        if lastopened[len(lastopened) -1] == 0:
            score += 1
        elif lastopened[len(lastopened) -1] == 1:
            score += 2
        elif lastopened[len(lastopened) -1] == 2:
            score += 3
        elif lastopened[len(lastopened) -1] == 3:
            score += 4
        lastopened.pop()
    return score

def check_rest(input):
    lastopened = []
    score = 0
    # Keep track of the brackets opened and then closed leaving those unclosed
    for bracket in input:
        if bracket == '(':
            lastopened.append(0)
        if bracket == '[':
            lastopened.append(1)
        if bracket == '{':
            lastopened.append(2)
        if bracket == '<':
            lastopened.append(3)
        if bracket == ')':
            lastopened.pop()
        if bracket == ']':
            lastopened.pop()
        if bracket == '}':
            lastopened.pop()
        if bracket == '>':
            lastopened.pop()
    score = complete_line(lastopened)
    return score


if __name__ == '__main__':
    lines = open("inputfile.txt").read().splitlines()

incomplete = []
point = 0
for line in lines:
    bracket = 0
    if bracket := check_corrupt(line):
        point += bracket
    else:
        incomplete.append(line)
points2 = []
for line in incomplete:
    points2.append(check_rest(line))
print(points2)
print(statistics.median(points2))