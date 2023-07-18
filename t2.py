from turtle import *

speed('fastest')
pencolor('green')
bgcolor('#999999')
pensize(4)

i = 100
while i > 0:
    fd(i)
    lt(90)
    i -= 4
    dot(10,'red')
    write(i, font=('Calibre', 20, 'bold'))

mainloop() #holds 