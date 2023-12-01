import sys
import re

with open(sys.argv[1]) as f:
    input = f.readlines()

digit_name_map = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

digit = re.compile("\d|" + "|".join(digit_name_map.keys()))

def extract_calibration(line):
    digits = [digit_name_map.get(d, d) for d in digit.findall(line)]
    return int(f"{digits[0]}{digits[-1]}")


print(sum(extract_calibration(line) for line in input))
