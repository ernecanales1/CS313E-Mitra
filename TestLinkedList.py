class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  def __len__(self):
    current = self.first
    size = 0
    while current is not None:
        size += 1
        current = current.next
    
    return size
  
  # get number of links 
  def getNumLinks (self):
    return len(self)
    
  # Add data at the beginning of the list
  def addFirst (self, data):
    newLink = Link(data)
    
    if self.isEmpty():
      self.first = newLink
    else:
      newLink.next = self.first
      self.first = newLink
      
  # Add data at the end of a list
  def addLast (self, data): 
    newLink = Link(data)
    if self.isEmpty():
      self.first = newLink
      return
    
    current = self.first
    while (current.next != None):
      current = current.next

    current.next = newLink
    
  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
    newLink = Link(data)
    if self.isEmpty():
      self.first = newLink
      return
      
    if not self.isSorted():
      return None

    current = self.first
    previous = self.first
    while(current.data < data):
        previous = current
        current = current.next
        if(current is None):
            break

    if current is None:
        self.addLast(data)
        return
    
    if current.data >= data:
        previous.next = newLink
        newLink.next = current
    
        
    elif previous.next != newLink:
      self.addLast(data)
      
  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
    current = self.first
    if self.isEmpty():
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current.data

  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
    if self.isEmpty():
      return None
    current = self.first
    
    if data < self.first.data:
      return None

    while current.data < data:
      if current.next == None:
        return None
      else:
        current = current.next
    if current.data != data:
      return None
    return current.data
  
  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
    count = 0
    if self.isEmpty():
      return False
    current = self.first
    previous = self.first

    while current != None:
      if previous.data <= current.data:
        count += 1
      previous = current
      current = current.next
    return count == len(self)
  
  

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    current = self.first
    previous = self.first

    if self.isEmpty():
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next
	
    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    string = ''
    if self.isEmpty():
      return None
    
    current = self.first
    
    while current != None:
      string +=  str(current.data) + "  "
      current = current.next
    
    return (string)

  # Copy the contents of a list and return new list
  def copyList (self):
    current = self.first
    newList = LinkedList()

    if self.isEmpty():
      return None
    
    while current != None:
      newList.addLast(current.data)
      current = current.next
    
    return newList
  
  # Return True if a list is empty or False otherwise
  def isEmpty (self): 
    return self.first == None
  # Reverse the contents of a list and return new list
  def reverseList (self): 
    newList = LinkedList()

    if self.isEmpty():
      return None
    current = self.first
    while current != None:
      newList.addFirst(current.data)
      current = current.next
      
    return (newList)

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
    current_a = self.first
    current_b = b.first
    print(current_b.data,current_a.data)
    c_length = self.getNumLinks() + b.getNumLinks()
    print(c_length)
    c = LinkedList()

    if current_a.data <= current_b.data:
        element = current_a.data 
        c.addFirst(element)
        current_a = current_a.next
    else:
        element = current_b.data 
        c.addFirst(element)
        current_b = current_b.next
    
    
    for i in range(c_length):
      if current_a
      if current_a.data <= current_b.data:
        element = current_a.data 
        c.addLast(element)
        current_a = current_a.next
      else:
        element = current_b.data 
        c.addLast(element)
        current_b = current_b.next
    return c
        
        
   
  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
    if b.isEmpty() and s.isEmpty():
      return True
    elif len(self) != len(b) or b.isEmpty() or self.isEmpty():
      return False
    
    current = self.first
    current_b = b.first
    while current != None and current_b != None:
      if current.data != current_b.data:
        return False
      current = current.next
      current_b = current_b.next

    return True

  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
    d = []
    current = self.first
    while current.next != None:
      e = current.data
      d.append(e)
      current = current.next
      self.delete(e)
    d.sort()
    for i in d:
      self.addInOrder(i)

    return self

  def removeDuplicates(self):
    current = self.first
    pivot = self.first
    for i in range(self.getNumLinks()):
      while current.next != None:
        if current.data == current.next.data:
          duplicate = current.data
          self.delete(duplicate)
        current = current.next
      pivot = current.next


    return self

  
      

          
          
        
      


      
    



def main():
  list1 = LinkedList()
  list1.addFirst(8)
  list1.addLast(4)
  list1.addLast(7)
  list1.addLast(4)
  list1.addLast(6)
  list1.addLast(9)
  list1.addLast(1)

  list2 = LinkedList()
  list2.addFirst(12)
  list2.addLast(5)

  list1.sortList()
  list2.sortList()

  print(list1.mergeList(list2))

  
  
  print(list1)
  list1.sortList()
  print(list1)
  list1.removeDuplicates()
  print(list1)

main()
