import sys
def qsort1 (a, lo, hi):
  if (lo >= hi):
    return

  pivot = a[lo]
  if (a.index(pivot) - 1 == len(a) // 2) and (len(a) % 2):
    print (a,a[lo-1])
    sys.exit()
  elif (a.index(pivot) - 1 == len(a) // 2) and (len(a) % 2 == 0):
    idx = len(a) // 2
    median = (a[idx] + a[idx-1]) / 2
    print(a, median)
    sys.exit()
  m = lo;
  for i in range (lo, hi + 1):
    if (a[i] < pivot):
      m = m + 1
      a[m], a[i] = a[i], a[m]
  
  a[lo], a[m] = a[m], a[lo]

  qsort1 (a, lo, m - 1)
  qsort1 (a, m + 1, hi)

def main():
  a = [9, 1, 8, 2, 7, 3, 6, 4, 5,4,2,5,7,1,12,13,8]
  print (a)
  qsort1 (a, 0, len(a) - 1)
  print (a)

main()
