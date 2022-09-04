import re
import string


def add(numbers):
    sum = 0
    if numbers == "":
        return 0
    numbers = re.split(",",numbers)
    for n in numbers:
        if n in string.ascii_lowercase:
            sum += string.ascii_lowercase.index(n) + 1
        else:
            sum += int(n)
    return sum