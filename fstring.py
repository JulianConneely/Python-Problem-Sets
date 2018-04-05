# Julian Conneely
# f strimg

for i in range(1, 11):
  print('{:2d} {:3d} {:4d} {:5d}' .format(i, i**2, i**3, i**4))

print("Another way to print using f-string below:")

for i in range(1, 11):
  print(f'{i:2d} {i**2:3d} {i**3:4d} {i**4:5d}')