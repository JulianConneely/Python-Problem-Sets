# Julian Conneely 06/04/18
# Exercise 6
# A function called factorial() that takes a single input/argument which is a positive integer and returns its factorial
# The factorial of a number is that number multiplied by all of the positive numbers less than it


def factorial(n):             #factorial is the function name and i is the argument(or info that is passed to a function, or Input) 
    number = 1                #this is the Output
    for i in range(1, n+1):   #i is a variable in the FOR loop representing the current element you are on in the range
        number=number*i       #Output is the number multiplied by the positive integer
    return number             #Not part of the FOR loop (indentation); return number and continue the loop while i is in the specified range (>=1)

# three seperate calls to the defined function
print("The factorial of number 5 is:",factorial(5))       # call the factorial function with 5 as the value n
print("The factorial of number 7 is:",factorial(7))       # call the factorial function with 7 as the value n
print("The factorial of number 10 is:",factorial(10))     # call the factorial function with 10 as the value n
