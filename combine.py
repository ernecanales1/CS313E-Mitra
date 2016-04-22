def combine (a, b, lo, size):
  hi = len(a)
  if (lo == hi):
    if (len(b) == size):
      print (b)
    return
  
  if (len(b) == size):
    print (b)
  else:
    c = b[:]
    b.append(a[lo])
    combine (a, c, lo + 1, size)
    combine (a, b, lo + 1, size)

def main():
  a = ['A', 'B', 'C', 'D', 'E', 'F']
  b = []
  combine (a, b, 0, 3)

main()
