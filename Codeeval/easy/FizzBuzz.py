import sys


def fizz_buzz(number, x, y):
    res = ""
    if number % x == 0:
        res = "F"
    if number % y == 0:
        res += "B"
    elif len(res) == 0:
        res = str(number)
    return res


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        arr = test.split()
        x = int(arr[0])
        y = int(arr[1])
        length = int(arr[2])
        for i in range(1, length + 1):
            result = fizz_buzz(i, x, y)
            if i < length:
                result += " "
            print(result, end='')
        print()
