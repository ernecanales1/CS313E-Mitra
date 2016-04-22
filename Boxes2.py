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

def subsets (a, b, lo):
  hi = len(a)
  if (lo == hi):
    if len(b)>1 :
      #print(b)
      best(b)
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1)
    subsets (a, b, lo + 1)

def best(alist):
  col1 = []
  col2 = []
  col3 = []
  
  for k in range(len(alist)):
    col1.append(alist[k][0])
    col2.append(alist[k][1])
    col3.append(alist[k][2])

  #print(col1)
  #print(col2)
  #print(col3)
  c1 = ascendingOrder(col1)
  c2 = ascendingOrder(col2)
  c3 = ascendingOrder(col3)
  
  
  if c1 and c2 and c3 :
    print(alist)
                      
  
    
def ascendingOrder(colList):
  a = 0
  for i in range(len(colList)-1):
    #print(colList[i+1])
    a += 1
  if a == (len(colList)-1):
    return True
  return False

def main():
    # read the file
    file = open("boxes.txt", 'r')
    
    #The first line gives the number of boxes n
    n = file.readline()

    #The next n lines gives a set of three integers separated by spaces
    sets = file.readlines()
    
    dimensions = []
    for line in sets:# read every line that cotains dimensions
        dimensions.append(line.split())
        for i in dimensions: #look up every group
          i = sorted(i)
          for x in i : # go through every number
                int(x)
                i.sort()
    
    b = []
    subsets(dimensions, b, 0)

main()


