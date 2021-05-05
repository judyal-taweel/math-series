def fibonacci(n):
    """
    for number 0 will return 0
    for number 1 will return 1
    for another numbers will sum (n-1)+(n-2)
    """
    return sum_series(n)

# print(fibonacci(7))
   
def lucas(n):
    """
    for number 0 will return 2
    for number 1 will return 1
    for another numbers will sum (n-1)+(n-2)
    """
    return sum_series(n,2,1)
# print(lucas(7))

def sum_series(n,x=0,y=1):
    """
    for didn't add number will use optional parameter x,y fibonacci(n)
    when add 2,1 will run as lucas(n)
    """
    if n >= 0:
      if n == 0:
        return x
      elif n == 1:
        return y  
      else:
          return sum_series(n-1,x,y) + sum_series(n-2,x,y)
    else:
        return "negative num is not allowed"
