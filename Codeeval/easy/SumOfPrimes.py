# CHALLENGE DESCRIPTION:
#
# Write a program which determines the sum of the first 1000 prime numbers.
import math


def is_prime(number):
    for i in range(2, number):
        if math.pow(i, 2) >= number and number % i == 0:
            return False
    return True


primeNumberSum = 0
primeNumberCounter = 0
index = 2

while primeNumberCounter < 1000:
    if is_prime(index):
        primeNumberSum += index
        primeNumberCounter += 1
    index += 1

print(primeNumberSum)
