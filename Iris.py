#Julian Conneely 28/03/18
#iris data set, Exercise 5

#with knows files, auto closes
with open("data/iris.csv") as f: #create a block of python code with f
  contents = f.read()
  print(contents)
