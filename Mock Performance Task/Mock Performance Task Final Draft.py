from cmu_graphics import *

Rect(0,0,1000,1000,fill='skyblue')
Rect(0,230,1000,230,fill='green')

Rect(200,200,10,200,fill=gradient('darkgreen','black',start='top'))
Layer1=Circle(150,200,50,fill=gradient('yellow','orange'))
Layer2=Circle(200,250,50,fill=gradient('yellow','orange'))
Layer3=Circle(250,200,50,fill=gradient('yellow','orange'))
Layer4=Circle(200,150,50,fill=gradient('yellow','orange'))
Layer5=Circle(200,200,50,fill='yellow', borderWidth=4, border='black')

def onMousePress(mouseX, mouseY):
     Layer5.fill=rgb(250, 177, 177)
     Layer2.fill=rgb(250, 127, 127)
     Layer3.fill=rgb(250, 127, 127)
     Layer4.fill=rgb(250, 127, 127)
     Layer1.fill=rgb(250, 127, 127)


def onMouseRelease(mouseX, mouseY):
     Layer5.fill=rgb(77, 43, 43)
     Layer2.fill=rgb(74, 28, 28)
     Layer3.fill=rgb(74, 28, 28)
     Layer4.fill=rgb(74, 28, 28)
     Layer1.fill=rgb(74, 28, 28)
cmu_graphics.run()
