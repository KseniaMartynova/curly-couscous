from turtle import*
shape("turtle")
speed(0)
color('blue')
pensize(1)

def fu(size, levels, angle):
    if levels==0:
        
        return
    #forward(size)
    right(angle)
    forward(size)
    fu(size*0.8,levels-1, angle)
    left(angle*2)
    fu(size*0.8,levels-1,angle)
    right(angle)
    left(angle*2)
    fu(size*0.8,levels-1,angle)
    right(angle)
    backward(size)

left(90)
right(90)

fu(50,5,60)

mainloop()

