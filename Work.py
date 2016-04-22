#  File: Work.py 

#  Description: This program calculates the minimum based on an algorithm

#  Student Name: Ernesto Canales

#  Student UT EID: egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 03/26/2015

#  Date Last Modified: 03/28/2015


def Work(v,k):
  # try for every number from 1 to v w/ equation
  for i in range(v):
    factorial = 0
    x = i // k
    t = 0
    while t < v:
      x = i // (k**factorial)
      factorial += 1
      if x == 0:
        break
      else:
        t += x
    if t >= v:
      print(i)
      break


def main():

  file = open('work.txt','r')
  cases = file.readline()
  cases = cases.strip()
  cases = int(cases)
  #interpret lines as v and k by creating a list
  for i in range(cases):
    line = list(file.readline())
    middle = line.index(' ')
    if '\n' in line:
      line.remove('\n')
    vl = line[:middle]
    kl = line[middle:]
    v = ''
    k = ''
    for x in vl:
      v += x
    v = int(v)
    for x in kl:
      k += x
    k = int(k)
        
    Work(v,k)
  file.close()

main()
    
  
      
    
    
    
  
  
