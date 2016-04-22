import math

class Point (object):
  # constructor
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # create a string representation of a Point
  def __str__ (self):
    return '(' + str (self.x) + ', ' + str (self.y) + ')'

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))
  
class Triangle(object):
  def __init__(self,ll_x,ll_y,lr_x,lr_y,pk_x,pk_y):
    if (ll_x < lr_x) and (pk_y > ll_y) and (pk_y > lr_y) and (ll_y == lr_y):
      self.ll = Point(ll_x,ll_y)
      self.lr = Point(lr_x,lr_y)
      self.pk = Point(pk_x,pk_y)
    else:
      self.ll = Point(0,0)
      self.lr = Point(1,0)
      self.pk = Point(1,2)
  def line_intersects(self,line):
    sidelp = Line(self.ll.x,self.ll.y,self.pk.x,self.pk.y)
    siderp = Line(self.lr.x,self.lr.y,self.pk.x,self.pk.y)
    if (line.slope() >= sidelp.slope()) and (line.y_intercept() >= sidelp.y_intercept()):
      return False
    if (

def main():
   t = Triangle(0,0,4,0,5,2)
   print(t.ll,t.lr,t.pk)

main()
      
    
