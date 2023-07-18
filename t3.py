from turtle import *

speed ('fastest')
colors = ['red' , 'yellow', 'blue', 'green','black']
pensize(2)
 
for i  in range (100):
    #print(i%5, colors[i%5])
    pencolor(colors[i%5])
    fd(i*2)
    lt(90)
    circle(i*2,30)
    
mainloop()       
