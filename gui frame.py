from tkinter import *

root=Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack()

redbutton = Button(frame, text="RED", fg="red")
redbutton.pack(side = LEFT)

greenbutton = Button(frame, text="GREEN", fg="green")
greenbutton.pack(side = LEFT)

yellowbutton = Button(frame, text="YELLOW", fg="yellow")
yellowbutton.pack(side = LEFT)

blackbutton = Button(frame, text="BLACK", fg="black")
blackbutton.pack(side = BOTTOM)

bluebutton = Button(frame, text="BLUE", fg="blue")
bluebutton.pack(side = TOP)

root.mainloop()
