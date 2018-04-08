# Julian Conneely 04/04/18
# Exercise 6
# A function called factorial() that takes a single input/argument which is a positive integer and returns its factorial
# The factorial of a number is that number multiplied by all of the positive numbers less than it

def factorial(i):           #factorial is the function name and i is the argument(or info that is passed to a function, or Input) 
    number = 1              #this is the Output
    while i>0:              #while i is a positive integer return its factorial (while conditions below)
        number=number*i     #Output is the number multiplied by the positive integer
        i = i - 1           #reduce i by 1 each loop and multiply by previous number (output)
    return number           #Not part of the while loop (indentation); return number and continue the loop while i>0, then close the loop

# three seperate calls to the defined function
print("The factorial of #5 is:",factorial(5))       # calls the factorial function with 5 as the value i
print("The factorial of #7 is:",factorial(7))       # calls the factorial function with 7 as the value i
print("The factorial of #10 is:",factorial(10))     # calls the factorial function with 10 as the value i
