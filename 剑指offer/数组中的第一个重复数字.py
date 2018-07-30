def duplicate(numbers, duplication):
    # write code here
    map = [0]*len(numbers)
    for i in numbers:
        if (map[i] == 1):
            duplication[0] = i
            return True
        map[i] = 1
    return False
duplication = [0]
print(duplicate([2, 1, 3, 1, 4], duplication))
print(duplication)
