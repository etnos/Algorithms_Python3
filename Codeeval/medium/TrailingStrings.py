# There are two strings: A and B. Print 1 if string B occurs at the end of string A. Otherwise, print 0.
#
# INPUT SAMPLE:
#
# The first argument is a path to the input filename containing two comma-delimited strings, one per line. Ignore all empty lines in the input file.
#
# For example:
#
# Hello World,World
# Hello CodeEval,CodeEval
# San Francisco,San Jose
#
# OUTPUT SAMPLE:
#
# Print 1 if the second string occurs at the end of the first string. Otherwise, print 0.
#
# For example:
# 1
# 1
# 0
import sys


def is_substring(str1, str2):
    str1len = len(str1)
    str2len = len(str2)

    if str1len < str2len:
        return False

    substring = str1[str1len - str2len:]
    return substring == str2


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        arr = test.split(",")
        if is_substring(arr[0].strip(), arr[1].strip()):
            print(1)
        else:
            print(0)
