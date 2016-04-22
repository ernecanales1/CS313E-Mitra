from turtle import Turtle
import random

def drawRectangle(t, x1, y1, x2, y2):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    # Code for drawing goes here

# Definition of the recursive mondrian function goes here



def mondrian(t, x1, y1, x2, y2, level):
    if level > 0:
        drawRectangle(t, x1, y1, x2, y2)
        vertical = random.randint(1, 2)
        if vertical == 1:   # Vertical split
            mondrian(t, x1, y1, (x2 - x1) // 3 + x1, y2,level - 1)
            mondrian(t, (x2 - x1) // 3 + x1, y1, x2, y2,level - 1)
        else:               # Horizontal split
            mondrian(t, x1, y1, x2, (y2 - y1) // 3 + y1,level - 1)
            mondrian(t, x1, (y2 - y1) // 3 + y1, x2, y2,level - 1)
            
def main(level = 1):
    t = Turtle()
    t.speed(7.0)
    t.hideturtle()
    x = 50
    y = 50
    mondrian(t, -x, y, x, -y, level)

main()
