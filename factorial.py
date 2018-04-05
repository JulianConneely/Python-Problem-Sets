# Julian Conneely 04/04/18
# Exercise 6
# define a function

def factorial(i):           #factorial is the function name and i is the argument(or info that is passed to a function, or Input) 
    number = 1              #this is the Output
    while i>0:              #while i is a positive integer return its factorial
        number=number*i     #Output is the number multiplied by the positive integer
        i = i - 1           #the positive integer should be minus 1
    return number           #return number and continue the loop while i is equal 1, then stop the loop

# three seperate calls to the defined functrion
print("The factorial of #5 is:",factorial(5))       # call the factorial function with 5 as the value i
print("The factorial of #7 is:",factorial(7))       # call the factorial function with 7 as the value i
print("The factorial of #10 is:",factorial(10))     # call the factorial function with 10 as the value i
