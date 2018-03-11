# Julian Conneely 09/03/2018
# https://projecteuler.net/problem=5
# What is the smallest number divisible by each of the numbers 1 to 20? 

i=20
while 1:
    i+=20   # is equivalent to i = i + 20
    if i%11==0 and i%12==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 \
        and i%17==0 and i%18==0 and i%19==0:
        print (i)
        break
