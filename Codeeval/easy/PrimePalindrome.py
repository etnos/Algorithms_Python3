import math


def is_prime(number):
    for i in range(2, number):
        if math.pow(i, 2) >= number and number % i == 0:
            return False
    return True


def is_palindrome(number):
    part1 = int(number / 100)
    part2 = int(number % 10 % 10)
    return part2 == part1

for i in reversed(range(900, 1001)):
    if is_palindrome(i):
        if is_prime(i):
            print(i)
            break
