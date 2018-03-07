# Julian Conneely, 07/03/2018
# Sum of all the odd numbers from 1 to 100

sum = 0
i = 0

while i <= 100:             # loop until 1 == 100
    if i % 2 == 1:          # stay in the loop if i divide by 2 leaves a remainder of 1  
        sum = sum + i       # 
    i = i + 1               # makes condition false and terminates the loop
                            # next line unindented and not part of the while loop, what happens when while loop finishes
print("The sum of odd numbers from 1 to 100 is:",sum)