# Julian Conneely, 2018-02-03
# A program that displays Fibonacci numbers
# My name is Julian, so the first and last letter of my name (J + N = 10 + 14) give the number 24. The 24th Fibonacci number is 46,368

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 24  
ans = fib(x)
print("Fibonacci number", x, "is", ans)
