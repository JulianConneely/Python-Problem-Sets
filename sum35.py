# Julian Conneely, 2018-09-14
# The Collatz conjecture program
# https://projecteuler.net/problem=1

sum = 0
i = 1

while i < 1000:
    if i % 3 == 0:
        sum = sum + i
    elif i % 5 == 0:
        sum = sum + i
    i = i + 1

print("Sum of multiples of 3 and 5, less than 1000:", sum)

