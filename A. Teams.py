import sys


contents = sys.stdin.read().split()
contents = [int(x) for x in contents]

rows = contents.pop(0)
result = 0

first_one = 0
second_one = 1
third_one = 2

while rows > 0:
    sum_of_row = contents[first_one] + contents[second_one] + contents[third_one]
    
    if sum_of_row >= 2:
        result += 1
    
    first_one += 3
    second_one += 3
    third_one += 3
    
    rows -= 1

print(result)
