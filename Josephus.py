#  File: Josephus.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:
"""
class Link(object):


class CircularList(object):
  # Constructor
  def __init__ ( self ): 

  # Insert an element in the list
  def insert ( self, item ):

  # Find the link with the given key
  def find ( self, key ):

  # Delete a link with a given key
  def delete ( self, key ):

  # Delete the nth link starting from the Link start 
  # Return the next link from the deleted Link
  def deleteAfter ( self, start, n ):

  # Return a string representation of a Circular List
  def __str__ ( self ):

"""
    

def main():
  #Read josephus.txt file
  file = open('josephus.txt','r')

  #Interpret input
  #Define amount of soldiers in group
  amount = file.readline()
  amount = amount.strip('\n')
  amount = int(amount)

  #Define starting point of soldiers
  start = file.readline()
  start = start.strip('\n')
  start = int(start)

  #Define elimination number
  elimination = file.readline()
  elimination = elimination.strip('\n')
  elimination = int(elimination)

  
  

    
  file.close()

main()



