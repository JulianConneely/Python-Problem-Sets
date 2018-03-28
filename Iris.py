# Julian Conneely 28/03/18
# Iris data set, Exercise 5

# With knows files, auto closes so no need to close

with open("data/iris.csv") as f: # create a block of python code with f as the name of the file that is open (iris.csv)
  for line in f:     
    a = line.split(',')  
    print(a[0],a[1],a[2],a[3],a[4])
