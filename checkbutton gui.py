from tkinter import *
root=Tk()
root.geometry('400x400')
root.resizable(0,1)
global b
global s
check = IntVar()
def cb():
    b=check.get()
    if(b==1):
        s="lol"
        label=Label(root,text=s)
        label.place(x=5,y=0)
    else:
        label=Label(root,text="          ")
        label.place(x=5,y=0)
        
#checkbutton                                          
c1=Checkbutton(text="lol",var=check,onvalue=1,offvalue=0,command=cb)

c1.pack()
root.mainloop()
