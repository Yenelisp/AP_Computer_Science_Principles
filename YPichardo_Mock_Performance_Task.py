from cmu_graphics import *

Rect(0,0,1000,1000,fill='skyblue')
Rect(0,230,1000,230,fill='green')

Rect(200,200,10,200,fill=gradient('black','black',start='top'))
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
     Rect(0,0,1000,1000,fill='pink')
     Rect(0,230,1000,230,fill='lightgreen')

     


def onMouseRelease(mouseX, mouseY):
     Layer1=Circle(150,200,60,fill=gradient('lightcoral','tomato'))
     Layer2=Circle(200,250,60,fill=gradient('lightcoral','tomato'))
     Layer3=Circle(250,200,60,fill=gradient('lightcoral','tomato'))
     Layer4=Circle(200,150,60,fill=gradient('lightcoral','tomato'))
     Layer5=Circle(245,150,50,fill=gradient('tomato','coral'))
     Layer6=Circle(145,150,50,fill=gradient('tomato','coral'))
     Layer7=Circle(145,255,50,fill=gradient('tomato','coral'))
     Layer8=Circle(250,255,50,fill=gradient('tomato','coral'))
     Layer9=Circle(200,200,50,fill='tomato', borderWidth=4, border='black')
     
    


     


def oMouseClick(mouseX,mouseY):
      Layer1=Circle(150,200,50,fill=gradient('yellow','orange'))
      Layer2=Circle(200,250,50,fill=gradient('yellow','orange'))
      Layer3=Circle(250,200,50,fill=gradient('yellow','orange'))
      Layer4=Circle(200,150,50,fill=gradient('yellow','orange'))
      Layer5=Circle(200,200,50,fill='yellow', borderWidth=4, border='black')
  


     
cmu_graphics.run()
