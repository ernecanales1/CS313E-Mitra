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

class Line (object):
  # constructor
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if ((abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol)):
      self.p1 = Point (0, 0)
      self.p2 = Point (1, 1)
    else:
      self.p1 = Point (p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs (self.p1.y - self.p2.y) < tol)

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    ...

  # determine slope for the line
  def slope (self):
    if (self.is_parallel_y()):
      return float ('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return (self.p1.y - (self.slope() * self.p1.x))

  # determine the x-intercept of the line
  def x_intercept (self):
    return (-1.0 * self.y_intercept()) / (self.slope())

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return (abs (self.slope() - other.slope()) < tol)

  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    ...

  # determine if a point is on the line 
  def is_on_line (self, p):
    ...

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    ...

  # determine the intersection point of two lines
  def intersection_point (self, other):
    ...

  # determine if two points are on the same side of the line
  def on_same_side (self, p1, p2):
    ...

  # string representation of the line
  def __str__ (self):
    ...

    
class Circle (object):
  # constructor
  def __init__ (self, radius = 0, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute circumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if a point is inside the circle
  def pointWithin (self, p):
    return (self.center.dist (p) < self.radius)
    # return (p.dist (self.center) < self.radius)

  # determine if a circle is strictly inside self
  def circleWithin (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  def circleIntersects (self, c):
    distance = self.center.dist (c.center)
    return distance < (self.radius + c.radius)

class Rectangle (object):
  # constructor defines a rectangle through two diagonally opposite points
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine the length 
  def length (self):
    return (self.lr.x - self.ul.x)

  # determine the width
  def width (self):
    return (self.ul.y - self.lr.y)

  # determine the perimeter
  def perimeter (self):
    return 2 * (self.length() + self.width())
  
  # determine the area
  def area (self):
    return self.length() * self.width()

  # determine if a point is inside the rectangle
  """
  def is_inside_point (self, p):
    if (p.x >= min(self.ul.x,self.lr.x)) and (p.x <= max(self.ul.x,self.lr.x)) and (p.y >= min(self.ul.y,self.lr.y)) and (p.y <= max(self.ul.y,self.lr.y)):
      return True
    else:
      return False

  
  # determine if a line (or its extension) intersects the rectangle
  def does_intersect_line (self, line):
    ...
  """
  # determine if the other rectangle overlaps self
  # return True if the two rectangles have any area in common
  
  def does_overlap_rect (self, other):
    
    if (other.ul.x > self.lr.x) or (other.lr.x < self.ul.x):
      return False
    elif (other.lr.y > self.ul.y) or (other.ul.y < self.lr.y):
      return False
    else:
      return True
      """
  def does_overlap_rect(self,other):
    if (self.ul.x <= other.ul.x) and (self.lr.x >= other.ul.x):
      if (self.lr.y <= other.ul.y) and (self.ul.y >= other.ul.y):
        return True
    if (self.ul.x <= other.lr.x) and (self.lr.x >= other.lr.x):
      if (self.lr.y <= other.lr.y) and (self.ul.y >= other.lr.y):
        return True
    else:
      return False
    """
    ...

  # string representation of a rectangle
  def __str__ (self):
    ...
    
def main():
  rec1 = Rectangle(0,3,3,0)
  rec2 = Rectangle(1,2,2,0)
  print(rec2.does_overlap_rect(rec1))

main()

