import sys

with open(sys.argv[1], 'r') as test_cases:
    reverse = lambda str: str.split(" ")[::-1]
    for test in test_cases:
        strip_test = test.strip()
        if len(strip_test) > 0:
            print(*reverse(strip_test))
