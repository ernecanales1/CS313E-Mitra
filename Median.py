def median(a,lo,hi):
  m = lo
  if lo >= hi:
    f = len(a) // 2
    if len(a) % 2:
      med = a[f]
    else:
      med = (a[f] + a[f-1]) / 2
    print (m,hi,med,a)
    return med
  pivot = a[lo]
  for i in range (lo, hi + 1):
    if (a[i] < pivot):
      m = m + 1
      a[m],a[i] = a[i],a[m]
  a[lo],a[m] = a[m],a[lo]
  median(a,lo,m-1)
  median(a,m+1,hi)

def main():
  a = [5,12,4,3,8,6,3,5,7,2]
  lo = 0
  hi = len(a) - 1
  print(len(a))
  median(a,lo,hi)


main()
  
