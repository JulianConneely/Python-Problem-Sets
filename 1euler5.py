# Julian Conneely 09/03/2018
# https://projecteuler.net/problem=5
# What is the smallest number divisible by each of the numbers 1 to 20? 


i = 1 
for k in (range(1, 21)):        # the FOR loop iterates over the sequence of numbers inisde the range 1 to 20
    if i % k > 0:               # if the remainder of i divide by k is greater than 0
        for j in range(1, 21):  #
            if (i*j) % k == 0:  #
                i *= j          # 
                break 
print (i)
