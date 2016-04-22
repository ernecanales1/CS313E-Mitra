#  File: TestBinaryTree.py

#  Description: Playing with a binary tree

#  Student Name: Ernesto Canales Medina

#  Student UT EID: egc536

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 04/18/2015

#  Date Last Modified: 04/19/2015

import random,sys
class Node (object):
  def __init__ (self, data):
    self.data = data
    self.lChild = None
    self.rChild = None

class Tree (object):
  def __init__ (self):
    self.root = None

  # Search for a node with the key
  def search (self, key):
    current = self.root
    while ((current != None) and (current.data != key)):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Insert a node in the tree
  def insert (self, val):
    newNode = Node (val)

    if (self.root == None):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild

      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode

  # In order traversal - left, center, right
  def inOrder (self, aNode):
    if (aNode != None):
      inOrder (aNode.lChild)
      print (aNode.data)
      inOrder (aNode.rChild)

  # Pre order traversal - center, left, right
  def preOrder (self, aNode):
    if (aNode != None):
      print (aNode.data)
      preOrder (aNode.lChild)
      preOrder (aNode.rChild)

  # Post order traversal - left, right, center
  def postOrder (self, aNode):
    if (aNode != None):
      postOrder (aNode.lChild)
      postOrder (aNode.rChild)
      print (aNode.data)

  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent
  

  # Delete a node with a given key
  def delete (self, key):
    deleteNode = self.root
    parent = self.root
    isLeft = False

    # If empty tree
    if (deleteNode == None):
      return False

    # Find the delete node
    while ((deleteNode != None ) and (deleteNode.data != key)):
      parent = deleteNode
      if (key < deleteNode.data):
        deleteNode = deleteNode.lChild
        isLeft = True
      else:
        deleteNode = deleteNode.rChild
    isLeft = False
      
    # If node not found
    if (deleteNode == None):
      return False

    # Delete node is a leaf node
    if ((deleteNode.lChild == None) and (deleteNode.rChild == None)):
      if (deleteNode == self.root):
        self.root = None
      elif (isLeft):
        parent.lChild = None
      else:
        parent.rChild = None

    # Delete node is a node with only left child
    elif (deleteNode.rChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.lChild
      elif (isLeft):
        parent.lChild = deleteNode.lChild
      else:
        parent.rChild = deleteNode.lChild

    # Delete node is a node with only right child
    elif (deleteNode.lChild == None):
      if (deleteNode == self.root):
        self.root = deleteNode.rChild
      elif (isLeft):
        parent.lChild = deleteNode.rChild
      else:
        parent.rChild = deleteNode.rChild

    # Delete node is a node with both left and right child
    else:
      # Find delete node's successor and successor's parent nodes
      successor = deleteNode.rChild
      successorParent = deleteNode

      while (successor.lChild != None):
        successorParent = successor
        successor = successor.lChild

      # Successor node right child of delete node
      if (deleteNode == self.root):
        self.root = successor
      elif (isLeft):
        parent.lChild = successor
      else:
        parent.rChild = successor

      # Connect delete node's left child to be successor's left child
      successor.lChild = deleteNode.lChild

      # Successor node left descendant of delete node
      if (successor != deleteNode.rChild):
        successorParent.lChild = successor.rChild
    successor.rChild = deleteNode.rChild

    return True

  # Returns true if two binary trees are similar
  def isSimilar(self,self_root,other_root):
    current= self_root
    current2= other_root
    if current == None and current2 ==None:
        return True
    else:
        if current !=None and current2 != None: 
            return current.data == current2.data and self.isSimilar(self_root.lChild,other_root.lChild) and self.isSimilar(self_root.rChild,other_root.rChild)
                
    return False

  def isFull(self, current, balanced):
    if balanced == False:
      return False
    if (current.lChild and current.rChild):
      balanced = True
      print('balanced')
      self.isFull(current.lChild,balanced)
      self.isFull(current.rChild,balanced)
      
    elif (current.lChild is None) and (current.rChild is None):
      balanced = True
      print('no children')
      return 
    else:
      print('unbalanced')
      balanced = False
      self.isFull(current,balanced)
      return False
    return False

    

  
  # Prints out all nodes at the given level
  def printLevel (self, level, branches, count):
    new_branches = []
    if count < level:
      for i in branches:
        if i.lChild:
          new_branches.append(i.lChild)
        if i.rChild:
          new_branches.append(i.rChild)
      self.printLevel(level,new_branches, count + 1)
    if count == level:
      for i in branches:
        print(i.data)
      return True
    
  
  # Returns the height of the tree
  def getHeight (self, self_root):
    current = self_root
    if current == None:
      return 0 
    
    left_height= self.getHeight(self_root.lChild)
    right_height = self.getHeight(self_root.rChild)
    if (left_height > right_height) :
        return left_height + 1 
    else:
        return right_height + 1

    

  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  """
  def numNodes(self, self_left, ):
    current = self_root
    if current == None:
      return 0
    else:
      return self.numNodes(self_root.lChild) + 1 + self.numNodes(self_root.rChild)
  """



  def numNodes(self, self_root):
    current = self_root
    if current == None:
      return 0
    else:
      a = []
      a.append(self.numNodes2(self_root.lChild))
      a.append(self.numNodes2(self_root.rChild))
      return a

  def numNodes2(self, self_root):
    current = self_root
    if current == None:
      return 0
    else:
      return self.numNodes2(self_root.lChild) + 1 + self.numNodes2(self_root.rChild)

    

    

  def countBranch(self,height,branches,count):
    if count < height:
      for i in branches:
        if i.lChild:
          branches.append(i.lChild)
        if i.rChild:
          branches.append(i.rChild)
      self.countBranch(height,branches, count + 1)
    if count == height:
      length = len(branches)
      print(length)
      return (int(length))
      



def main():

    
    # Create three trees - two are the same and the third is different
    one = Tree()
    
    one.insert(50)
    one.insert(30)
    one.insert(70)
    one.insert(10)
    one.insert(40)
    one.insert(60)
    one.insert(80)
    one.insert(7)
    one.insert(25)
    one.insert(38)
    one.insert(47)
    one.insert(58)
    one.insert(65)
    one.insert(77)
    one.insert(96)
    two = one
    
    five = Tree()
    five.insert(65)
    five.insert(12)
    five.insert(24)
    five.insert(13)
    five.insert(54)
    five.insert(47)
    five.insert(89)
    five.insert(73)
    five.insert(31)
    five.insert(16)
    

  
    # Test your method isSimilar()
    print("Is tree one the same as tree two?", one.isSimilar(one.root,two.root))
    print("Is tree one the same as tree two?", five.isSimilar(five.root,one.root))
    # Print the various levels of two of the trees that are different
    print("Test printLevels() in tree one")
    one_root = [one.root]
    for i in range (1,5):
      print("The nodes in level", i ,"are: ")
      one.printLevel(i,one_root,1)

    print("Test printLevels() in tree five")
    five_root = [five.root]
    for i in range (1,7):
      print("The nodes in level", i ,"are: ")
      one.printLevel(i,five_root,1)


    # Get the height of the two trees that are different
    print("Testing getHeight()")
    print("Height of tree one: ", one.getHeight(one.root))
    print("Height of tree five: ", five.getHeight(five.root))
    
  
    # Get the number of nodes in the left and right subtree
    print("Number of nodes in tree one")
    one_root = one.root
    print(one.numNodes(one_root))

    print("Number of nodes in tree five")
    five_root = five.root
    print(five.numNodes(five_root))

    #check is full
    print('isFull()')
    print(one.isFull(one_root,True))



main()
