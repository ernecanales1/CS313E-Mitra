def subsets (a, b, lo):
  global lisst
  global mindif
  hi = len(a)
  if (lo == hi):
    if abs(sum(b)-(s-sum(b)))<=mindif:
      mindif = abs(sum(b)-(s-sum(b)))
      lisst=b
      return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)

def main():
  a = [5,5,10,20,25,30,35,50,100]
  global s
  s = sum(a)
  global mindif
  mindif = s
  b = []
  subsets (a, b, 0)
  for i in lisst:
  	a.remove(i)
  print(a,lisst)
main()
