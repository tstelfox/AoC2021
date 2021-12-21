

def make_caves(lines):
    temp = []
    lines = [x.split('-') for x in lines]
    for connection in lines:
        for thing in connection:
            if thing not in temp:
                temp.append(thing)
    caves = [[val] for val in temp]
    for connection in lines:
        for i, thing in enumerate(connection):
            for x, item in enumerate(caves):
                if i == 0:
                    # print("Cave", item)
                    # print("Connection", thing)
                    if item[0] == thing:
                        caves[x].append(connection[1])
                elif i == 1:
                    if item[0] == thing:
                        caves[x].append(connection[0])
    # caves.pop()
    return caves


def backin_up(nodes, current):
    if nodes[current][0] == 'end':
        return
    for path in nodes[current][1:]:
        backin_up(nodes, )
    # count = 1

    print(nodes)
    # print(current)

    # return 0


if __name__ == '__main__':
    lines = open('testfile.txt').read().splitlines()
    caves = make_caves(lines)
    routes = 0
    start_id = 0
    # end_id = 0
    while caves[start_id][0] != 'start':
        start_id += 1
    # while caves[end_id][0] != 'end':
    #     end_id += 1
    backin_up(caves, start_id)



