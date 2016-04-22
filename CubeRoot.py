def binarySearch(a):
  lo = 0
  hi = max(1.0,a)
  mid = (lo + hi) / 2
  tol = 1.0e-11

  while (abs(mid**3 - a) > tol):
    if (a > mid**3):
      lo = mid
    elif (a < mid**3):
      hi = mid
    mid = (lo + hi) / 2

  return mid

def main():
  
  num = .5
  q = binarySearch(num)
  print(round(q,10))

main()

