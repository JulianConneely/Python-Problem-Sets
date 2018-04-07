# Julian Conneely 09/03/2018
# https://projecteuler.net/problem=5
# What is the smallest number divisible by each of the numbers 1 to 20? 

i=20
while 1:
    i+=20   # is equivalent to i = i + 20
    # Any integer evenly divisible by 20 is evenly divisible by 2 
    # (but the reverse might not be true). So we leave the 20 and take out the 2, the 4, and the 5
    # Leave the 19, as it's prime. Leave the 18, but now we can take out the 3 and the 6
    # If you repeat this process, you wind up with a much shorter list of numbers to try
    if i%11==0 and i%13==0 and i%14==0 and i%16==0 \
        and i%17==0 and i%18==0 and i%19==0:
        print (i)
        break
