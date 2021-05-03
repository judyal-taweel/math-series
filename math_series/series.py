def fibonacci(n):
   return sum_series(n)

# print(fibonacci(7))
   
def lucas(n):
    return sum_series(n,2,1)
# print(lucas(7))

def sum_series(n,x=0,y=1):
    if n >= 0:
      if n == 0:
        return x
      elif n == 1:
        return y  
      else:
          return sum_series(n-1,x,y) + sum_series(n-2,x,y)
    else:
        return "negative num is not allowed"
