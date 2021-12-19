
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

def check_line(input):
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


if __name__ == '__main__':
    lines = open("inputfile.txt").read().splitlines()

point = 0
for line in lines:
    bracket = 0
    if bracket := check_line(line):
        # print(bracket)
        point += bracket
print(point)
