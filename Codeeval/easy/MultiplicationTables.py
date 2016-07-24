def get_formatted_number(number):
    result = ""
    if number < 1000:
        result += " "
        if number < 100:
            result += " "
            if number < 10:
                result += " "
                result += str(number)
            else:
                result += str(number)
        else:
            result += str(number)
    else:
        result += str(number)

    return result

for x in range(1, 13):
    for y in range(1, 13):
        print(get_formatted_number(x * y), end="")
    print()
