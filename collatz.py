# Julian Conneely, 2018-23-02
# The Collatz conjecture program

n = int(input("Please enter an integer: "))
while n != 1:       # while n is not equal to 1 do this
  if (n % 2 == 0):  # this is an even number
    n = n // 2      # n should be divided by 2 with // indicating no decimal points
    print (n)       # print n in the integrated terminal
  elif n % 2 != 0:  #this is an odd number
    n = (n * 3) + 1 # n should be multiplied by 2 with and add 1
    print (n)       # print n in the integrated terminal 

print ("the final value of n is 1")