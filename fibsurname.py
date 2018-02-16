# Julian Conneely, 2018-02-05
# A program that displays Fibonacci numbers using people's names.
# My surname is Conneely The first letter C is number 67 The last letter y is number 121 Fibonacci number 188 is 871347450517368352816615810882615488381
# ord() returns an integer (or decimal) representing the Unicode code point of that character

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Conneely"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
