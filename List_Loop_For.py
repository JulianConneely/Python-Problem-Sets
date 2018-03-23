#Julian Conneely, 23/03/18
#List Loop and For and Range


squares = [1,4,9,16,25]     #creating the list
i=0                     
while i < len(squares):     #while i is less than the length of the list (no of elements in the list 0 1 2 3 4)
    print(i, squares[i])    #print i and the item from the list
    i = i + 1               #increment i preventing endless loop


words = ['cat', 'window', 'defenestrate']   #creating the list
for x in words:                             #For statement iterates over the items of any sequence (a list or a string), in the order that they appear in the sequence
    print(x, len(x))                        #print x and the length of x  

for i in range(len(words)):                 #range creates a mini list in background 0, 1, 2
    print(i, words[i], len(words[i]))       #prints i (0 1 or 2); words (list element) and the length of i

