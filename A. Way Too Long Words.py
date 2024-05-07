import sys

stack = []

words = sys.stdin.read().split('\n')

words = words[1:]

for word in words:
    if len(word) <= 10:
        stack.append(word)
        continue
    
        
    
    first_letter = word[0]
    last_letter = word[-1]
    number_of_letters = len(word) - 2
    
    stack.append(first_letter + str(number_of_letters) + last_letter)

output = "\n".join(stack)
sys.stdout.write(output)
