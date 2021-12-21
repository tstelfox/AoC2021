

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
                    print("Cave", item)
                    print("Connection", thing)
                    if item[0] == thing:
                        print("hey")
                        caves[x].append(connection[1])
                elif i == 1:
                    if item[0] == thing:
                        caves[x].append(connection[0])
    print(caves)


if __name__ == '__main__':
    lines = open('testfile.txt').read().splitlines()
    make_caves(lines)



