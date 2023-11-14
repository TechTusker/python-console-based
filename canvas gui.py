from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.geometry('800x800')
root.resizable(0,1)
x1=0
y1=0
h=60
w=60
canvas = Canvas(root,width=500, height=300, bg='yellow')
canvas.pack()
canvas.create_rectangle(20,100,70,180, fill='red')
canvas.create_line(100,200,200,35, fill='green', width=6)
canvas.create_oval(20,100,70,180, fill='blue')
iu1 = ImageTk.PhotoImage(Image.open("14.jpg"))
canvas.create_image(50,50, image=iu1)

rect = canvas.create_rectangle(0,0,20,20)
canvas.itemconfigure(rect, fill='red')

def move():
    global x1
    global y1
    global w
    global h
    x1=x1+10
    w=w+5
    canvas.coords(rect,x1,0,w,60)
    #canvas.delete(rect)

def go():
    global x1
    global y1
    x1=x1+10
    c.place(x=x1,y=0)

b=Button(canvas,text='move',bg='green',width=10,command=go)
b.place(x=200,y=200)
c=Button(canvas,text='go',bg='orange',width=10)
#canvas.delete(ALL)

root.mainloop
