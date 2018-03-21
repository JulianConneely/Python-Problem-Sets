#Julian Conneely, 21/03/18
#WhileIF loop with increment

#first 5 is printed
#then it is decreased to 4
#as it is not satisfying i<=2
#it moves on
#then 4 is printed
#then it is decreased to 3
#as it is not satisfying i<=2,it moves on
#then 3 is printed
#then it is decreased to 2
#as now i<=2 has completely satisfied, the loop breaks 

i = 5
while True:
    print(i)
    i=i-1
    if i<=2:
        break
