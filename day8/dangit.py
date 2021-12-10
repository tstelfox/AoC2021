global wires

def Diff(list1, list2):
    return list(set(list1) - set(list2)) + list(set(list2) - set(list1))

def check_equality(list1, list2):
    if len(list1) != len(list2):
        return False
    return sorted(list1) == sorted(list2)

def has_all(string, chars):
    return all([char in string for char in chars])


def final_four(digits, nums):
    four = ""
    for numero in nums:
        i = 0
        for first_numbers in digits:
            if numero == first_numbers:
                four.add(four, str(i))
            i += 1
    # print(four)
    return 1

def first_deduction(found, digit, wires):
    for thing in found[7]:
        if thing not in found[1]:
            wires[0] = thing

    return wires

def remaining_digits(found, digit, wires):
    wires = first_deduction(found, digit, wires)
    for letters in digit:
        if len(letters) == 5 and has_all(letters, list(found[1])):
            found[3] = letters
        temp = found[4] + wires[0]
        if len(letters) == 6 and has_all(letters, list(temp)):
            found[9] = letters
        wires[4] = Diff(list(found[9]), list(found[8]))
        left = Diff(list(found[8]), list(found[3]))
        wires[5] = Diff(left, list(wires[4]))
        if Diff(list(letters), list(found[3])) == wires[5]:
            found[2] = letters
        if len(letters) == 5 and wires[4][0] not in letters and wires[5][0] in letters:
            found[5] = letters
        if Diff(list(letters), list(found[5])) == wires[4]:
            found[6] = letters
    # print(Diff(found, digit))
    # if found[2] != '2':
    #     for sides in found[2]:
    #         if found[1][0] == sides:
    #             wires[2] = found[1]
    #             wires[1] = found[0]
    #         elif found[1][1] == sides:
    #             wires[2] = found[0]
    #             wires[1] = found[1]




    print(found)
    print(digit)
    return found

def ten_digits(data):
    wires = [i for i in range(7)]
    found = [str(i) for i in range(10)]
    digit = data.split()
    for letters in digit:
        if len(letters) == 2:
            found[1] = letters
        if len(letters) == 3:
            found[7] = letters
        if len(letters) == 4:
            found[4] = letters
        if len(letters) == 7:
            found[8] = letters
    while not check_equality(found, data):
        found = remaining_digits(found, digit, wires)
    print(found)
    print(data)
    return found


lines = open('inputfile').read().split('\n')
numbers = []
the_sum = 0
for line in lines:
    sections = line.split('|')
    numbers = ten_digits(sections[0])
    the_sum += final_four(numbers, sections[1])
    break