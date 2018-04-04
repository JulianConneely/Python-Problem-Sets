# Julian Conneely 04/04/18
# Exercise 6

#define a function
#sumall is a block of code that takes an input and gives an output
def sumall(upto):
  sumupto = 0
  for i in range (1, upto + 1):
    sumupto = sumupto + 1
  return sumupto #output or point of the function

print("The sum of the values from 1 to 50 inclusive is: ", sumall(50)) # calls the sumall function with 50 as the value upto
print("The sum of the values from 1 to 5 inclusive is: ", sumall(5))



def gcd(x, y):
  while x != 0 and y != 0:
    if x > y:
      x = x % y
    else:
      y = y % x
  if x ==0:
    return y
  else:
      return x

print("GCD of 6 and 15:", gcd(6, 15))
