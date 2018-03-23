#Julian Conneely 23/03/18
#using len (list)

#print the first element of the list, if it contains even number of elements.

list = [1, 2, 3, 4]
if len(list) % 2 == 0:
    print(list[0])