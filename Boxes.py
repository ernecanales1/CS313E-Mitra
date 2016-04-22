#  File: Boxes.py
#  Description:
#  Student Name:
#  Student UT EID:
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 
#  Date Created:
#  Date Last Modified:
##############################################################################

# order does not matter Combination
maxim = []
m = 0
def subsets (a, alist, lo, sets):
  hi = len(a)
  if (lo == hi):
    if len(alist) > 1:
      if alist == sorted(alist):
        return (get_set(alist, sets))
  else:
    c = alist[:]
    alist.append (a[lo])
    subsets (a, c, lo + 1, sets)
    subsets (a, alist, lo + 1, sets)

def get_set(alist, sets):
  sub_list = []
  for i in alist:
    sub_list.append(sets[i])
  return(col_arrange(sub_list))

def col_arrange(alist):
  col1 = []
  col2 = []
  col3 = []
  
  for k in range(len(alist)):
    col1.append(alist[k][0])
    col2.append(alist[k][1])
    col3.append(alist[k][2])

  if (CheckOrder(col1) != 1) and (CheckOrder(col2) != 1) and (CheckOrder(col3) != 1):
    check_max((alist))

def CheckOrder(col):
  a = 0
  for i in range(len(col)-1):
    if col[i] >= col[i+1]:
      a = 1
  return (a)

def check_max(alist):
  global maxim
  global m
  if len(alist) >= m:
    maxim += [alist]
    m = len(alist)
  
    
def main():
    # read the file
    file = open("boxes.txt", 'r')
    sets = []
    indices = []
    #The first line gives the number of boxes n
    n = int(file.readline())
    

    #The next n lines gives a set of three integers separated by spaces
    for line in range(n):
      sets.append(file.readline().split())
    file.close()

    for num in range(len(sets)):
      sets[num].sort()
      indices += [num]
    sets.sort()

    
    b = []
    
    subsets(indices, b, 0, sets)
    global maxim
    
    for i in range(len(maxim)-1, 1, -1):
      if len(maxim[i-1]) < len(maxim[i]):
        maxim.remove(maxim[i-1])
    maxim.remove(maxim[0])
    maxim.sort()
    print(maxim)
    
main()


