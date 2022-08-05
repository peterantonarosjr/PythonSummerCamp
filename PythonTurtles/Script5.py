import turtle
import random
from turtle import *

turtle.title("rainbow spiral")
speed(0)
bgcolor("black")

l1 = []
l2 = []
for i in range(0,30):
    n1 = random.randint(-800,800)
    n2 = random.randint(-600,600)
    l1.append(n1)
    l2.append(n2)


list = [list(l) for l in zip(l1, l2)]
for spot in list:
    penup()
    goto(spot[0],spot[1])

    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    #r,g,b=255,0,0
    colormode(255)
    pendown()
    size = random.randint(10,200)
    size2 = random.randint(10,40)
    shape = random.randint(45,120)
    for i in range(size):
        colormode(255)
        if i<size//3:
            g+=3
            if g>255:
                g=0
        elif i<size*2//3:
            r-=3
            if r<0:
                r=255
        elif i<size:
            b+=3
            if b>255:
                b=0
        elif i<size*4//3:
            g-=3
            if g<0:
                g=255
        elif i<size*5//3:
            r+=3
            if r>255:
                r=0
        else:
            b-=3
            if b<0:
                b=255
        fd((size/size2)+i)
        rt(shape)
        pencolor(r,g,b)

done()
