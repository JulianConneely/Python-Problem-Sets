# Julian Conneely 09/03/2018
# https://projecteuler.net/problem=5
# What is the smallest number divisible by each of the numbers 1 to 20? 

i=20
while 1:
    i+=20   # is equivalent to i = i + 20

    # starting with i=20 beacuse the asn must be divisible by 20
    # Any integer evenly divisible by 18 is also evenly divisible by 2 9 6 and 3 etc so we can exclude these etc
    # Leave prime numbers like 19 17 13 11
    # 7 covered by 14 etc
    # So we repeat this process ending up with a much shorter list of numbers to try
    if i%11==0 and i%13==0 and i%14==0 and i%15==0 and i%16==0 and i%17==0 and i%18==0 and i%19==0:
        print (i)
        break
