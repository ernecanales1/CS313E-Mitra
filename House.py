import turtle
import math
def drawPolygon (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  count = 1
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)

def drawRectangle (ttl, x, y, num_side, radius):
  sideLen = 2 * radius * math.sin (math.pi / num_side)
  angle = 360 / num_side
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  count = 1
  for iter in range (num_side):
    ttl.forward (sideLen)
    ttl.left (angle)

def main():
  # draw a triangle
  turtle.pensize(3)
  turtle.penup()
  turtle.goto (20, 50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('red')
  turtle.circle (-40, steps = 3)
  turtle.end_fill()

  # draw a square
  turtle.penup()
  turtle.goto (-100, -50)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color ('navy')
  turtle.circle (40, steps = 4)
  turtle.end_fill()
  ttl = turtle.Turtle()
  drawPolygon (ttl, -50, -50, 4,50)
main()
