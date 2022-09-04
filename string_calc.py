import re


def add(numbers):
    sum = 0
    if numbers == "":
        return 0
    numbers = re.split(",",numbers)
    for n in numbers:
        sum += int(n)
    return sum