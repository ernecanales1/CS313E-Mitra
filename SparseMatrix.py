#  File: SparseMatrix.py

#  Description: multiplies and adds matrices

#  Student Name: Ernesto Canales

#  Student UT EID: egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 04/16/2015 

#  Date Last Modified: 04/16/2015


class Link (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = None



class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row      # number of rows
    self.num_cols = col      # number of columns
    self.matrix = None

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create new link
    newLink = Link (row, col, data)


    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return

    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next
      
    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

  # return a row of the sparse matrix
  def getRow (self, row_num):
    # create a blank list
    a = []
    # search for the row
    current = self.matrix
    if (current == None):
      return a
    while ((current != None) and (current.row < row_num)):
      current = current.next
    if ((current != None) and (current.row > row_num)):
      for i in range (self.num_cols):
        a.append (0)
      return a
    if ((current != None) and (current.row == row_num)):
      for j in range (self.num_cols):
        if (current.col == j) and current.next != None:
          a.append (current.data)
          current = current.next
        elif (current.col == j) and current.next == None:
          a.append (current.data)
        else:
          a.append (0)
    return a
        

  # returns a column of the sparse matrix
  def getCol (self, col_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if (current == None):
      return a

    while ((current != None) and (len(a) != self.num_rows)):
      if current.col == col_num:
        if current.row >= len(a):
          for i in range(current.row - len(a)):
            a.append(0)
        a.append(current.data)
        
        
      current = current.next
    if len(a) < self.num_rows:
      for i in range(self.num_rows - len(a)):
        a.append(0)

    return a
  # adds two sparse matrices
  def __add__ (self, other):

    a = SparseMatrix(self.num_rows,other.num_cols)
    row = 0
    for i in range(self.num_rows):
      new_row = []
      row_A = self.getRow(i)
      row_B = other.getRow(i)
      for j in range (len(row_A)):
        new_row.append(row_A[j] + row_B[j])
      for k in range(len(new_row)):
        a.insertLink(row,k,new_row[k])
      row += 1

    return a





  # multiplies two sparse matrices
  def __mul__ (self, other):

    new_matrix = SparseMatrix(self.num_rows, other.num_cols)
    new_row = []
    row=0
    
    for i in range(self.num_rows):
      row1 = self.getRow(i)
      for x in range(self.num_cols):
        col1 = other.getCol(x)
        sum = 0
        for j in range(len(row1)):
          sum += row1[j]* col1[j]
        new_row.append(sum)
      for k in range(len(new_row)):
        new_matrix.insertLink(row,k,new_row[k])
      new_row = []
      row+=1
      
    return new_matrix
    
    

  # returns a string representation of a matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data) + " "
          current = current.next
        else:
          s = s + "0 "
      s = s + "\n"

    return s

  
# reads the matrix from a file
def readMatrix (inFile):
  line = inFile.readline()
  line = line.strip()
  line = line.split()
  row = int (line[0])
  col = int (line[1])

  mat = SparseMatrix (row, col)

  for i in range (row):
    line = inFile.readline()
    line = line.strip()
    line = line.split()
    for j in range (col):
      data = int (line[j])
      if (data != 0):
        mat.insertLink (i, j, data)
 
  # dummy read
  line = inFile.readline()

  return mat

def main():
  # populate the matrix
  inFile = open ("matrix.txt", "r")

  print ("Test Matrix Addition")
  matA = readMatrix (inFile)
  print (matA)

  matB = readMatrix (inFile)
  print (matB)


  matC = matA + matB
  print (matC)
  

  print ("\nTest Matrix Multiplication") 
  matP = readMatrix (inFile)
  print (matP)
  matQ = readMatrix (inFile)
  print (matQ)


  matR = matP * matQ
  print (matR)


  # close file
  inFile.close()

main()
