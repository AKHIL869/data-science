from turtle import *
speed('slowest')
pencolor('blue')
pensize(3)

#range(stop value)
#range(start,stop)
#range(start,stop,step)

for i in range(1,20,2):
    fd(60)
    rt(360/10)
    dot(10, 'Green')
    write(i, font=('Calibre', 20, 'bold'))

#reverse
goto(100,100)
for i in range(10,0,-1):
    fd(60)
    lt(360/10)
    dot(20, 'red')
    write(i, font=('Calibre', 20, 'bold'))
    mainloop()
       

