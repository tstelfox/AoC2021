def check_equality(list1, list2):
    if len(list1) != len(list2):
        return False
    return sorted(list1) == sorted(list2)


def check_sorted(list1, list2):
    list1 = sorted(list1)
    list2 = sorted(list2)

    return check_equality(list1, list2)


def count_common(first, second):
    cnt = 0
    for c in second:
        for char in first:
            if char == c:
                cnt += 1
    return cnt


def final_four(numbers, code):
    cnt = [0 for _ in range(4)]
    codenum = 0
    finalnum = 0
    code = code.split()
    for digit in code:
        for solution in numbers:
            if check_sorted(solution, digit):
                cnt[finalnum] = codenum
            codenum += 1
        finalnum += 1
        codenum = 0
    calculated = int(cnt[0] * 1000)
    calculated += int(cnt[1] * 100)
    calculated += int(cnt[2] * 10)
    calculated += int(cnt[3])
    return calculated


def ten_digits(data):
    found = [str(i) for i in range(10)]
    digits = data.split()
    # Find the unique numbers
    for value in digits:
        if len(value) == 2:
            found[1] = value
        if len(value) == 3:
            found[7] = value
        if len(value) == 4:
            found[4] = value
        if len(value) == 7:
            found[8] = value
    # Find the subsequent bastards
    # while not check_equality(found, data):
    for i in range(10):
        for value in digits:
            if len(value) == 5:
                if count_common(found[1], value) == 2:
                    found[3] = value
                if found[3] != value and count_common(found[9], value) == 5:
                    found[5] = value
                if found[5] != value and count_common(found[3], value) == 4:
                    found[2] = value
            if len(value) == 6:
                if count_common(found[3], value) == 5:
                    found[9] = value
                if found[9] != value and count_common(found[5], value) == 5:
                    found[6] = value
                if found[6] != value and found[9] != value and count_common(found[8], value) == 6:
                    found[0] = value
    return found


lines = open('inputfile').read().split('\n')
numbers = []
the_sum = 0
for line in lines:
    sections = line.split('|')
    numbers = ten_digits(sections[0])
    the_sum += final_four(numbers, sections[1])

print(the_sum)