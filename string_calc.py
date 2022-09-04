import re
import string

from MyExceptions import NegativeValueException


def add(numbers):
    sum = 0
    neg_nums = []
    if numbers == "":
        return 0
    numbers = re.split(",",numbers)
    for n in numbers:
        if n in string.ascii_lowercase:
            sum += string.ascii_lowercase.index(n) + 1
        else:
            if int(n) < 0:
                neg_nums.append(int(n))
            sum += int(n)
    if len(neg_nums) != 0:
        raise NegativeValueException("Negatives not allowed"+str(neg_nums))
    return sum