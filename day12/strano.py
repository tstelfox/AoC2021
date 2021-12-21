

def make_caves(lines):
    temp = []
    lines = [x.split('-') for x in lines]
    for connection in lines:
        for thing in connection:
            if thing not in temp:
                temp.append(thing)
    caves = [[val] for val in temp]
    # for node in caves:

        # if connection[0] not in temp:
        #     temp.append(connection[0])
        # if connection[1] not in temp:
        #     temp.append(connection[1])
    #     connection = connection.split('-')
    #     print(connection)
    # print(lines)
    print(caves)


if __name__ == '__main__':
    lines = open('testfile.txt').read().splitlines()
    make_caves(lines)


