from os import path
import re

with open("input.txt") as f:
    input = f.read() 
pattern = r'[6-9]\d{9}'
mobile_numbers = re.findall(pattern, input)

print(mobile_numbers)

with open("output.txt", "w") as f:
    for n in mobile_numbers:
        f.write(n + '\n')
