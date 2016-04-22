class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class CircularList(object):
  def __init__(self):
    self.head = Link(None, None)
    self.head.next = self.head

  def __str__(self):
    a = "["
    current = self.first
    while current != None:
      a += str(current.data) + ',' 
      current = current.next
    a = a[:-2] + ']'  
    return a  

  def InsertLast(self, item):
    NewLink = Link(item)
    current = self.first

    if current == None:
      self.first = NewLink  
      return 

    while current.next != None:
      current = current.next
    current.next = Link(item)

  def find (self, data):
    current = self.first
    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteAfter(self,start,n):
    s_pos = self.find(start)

    kill = self.find(start + n)

    n_pos = self.find(start + n + 1)

    
