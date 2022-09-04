import re
import string

from MyExceptions import NegativeValueException


def add(numbers):
    sum = 0
    neg_nums = []
    if numbers == "":
        return 0
    if len(re.findall("//.\n",numbers)) != 0:
        delim = numbers[2]
        numbers = numbers[4:]
        numbers = re.split(",|\n|"+delim,numbers)
    else:
        numbers = re.split(",|\n",numbers)
    for n in numbers:
        if n in string.ascii_lowercase:
            sum += string.ascii_lowercase.index(n) + 1
        elif int(n) > 1000:
            pass
        else:
            if int(n) < 0:
                neg_nums.append(int(n))
            sum += int(n)
    if len(neg_nums) != 0:
        raise NegativeValueException("Negatives not allowed"+str(neg_nums))
    return sum