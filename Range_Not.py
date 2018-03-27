#Julian Conneely 23/03/18
#using Range and Not


# Teh range is [0,1,2,3,4,5,6,7,8,9] 
#0%2=0 so nothing is printed 
#1%2=1 so 1 + 1 = 2 
#2%2=0 so nothing is printed 
#3%2=1 so 3 + 1 = 4 
#4%2=0 so nothing is printed 
#5%2=1 so 5 + 1 = 6 
#6%2=0 so nothing is printed 
#7%2=1 so 7 + 1 = 8 
#8%2=0 so nothing is printed 
#9%2=1 so 9 + 1 = 10

for i in range(10):
    if not i % 2 == 0:
	    print (i + 1) 
