def Pancake(a):
  a.sort()
  count = 0
  end = len(a) - 1
  for i in  range ((len(a) ) // 2):
    a[i],a[end - count] = a[end-count],a[i]
    count += 1
def main():

  a = [1,2,3,4,5,6,7,8,9,10,11]
  Pancake(a)
  print(a)

main()
    
    
    
