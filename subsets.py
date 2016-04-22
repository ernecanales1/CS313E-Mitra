import sys
def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    d = set(a) - set(b)
    d = list(d)
    if sum(d) - sum(b) == 0:
      print(b,d)
      print('True')
      sys.exit()
    return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)

def main():
  a = [15, 16,1,3,5,6,2,3,4,1,1,1,1,1]
  b = []
  if not subsets (a, b, 0):
    print("False")
  

main()
