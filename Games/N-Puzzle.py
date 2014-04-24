from Tkinter import *
import random

def swap(bx, by, x, y):
    num = app.numbers[x][y]['text']
    app.numbers[x][y].config(bg='grey', text='')
    app.numbers[bx][by].config(bg='SteelBlue', text=num)
    app.blankX, app.blankY = x, y

def key(event):
    bx, by = app.blankX, app.blankY
    if event.keysym=='Up' and bx<app.size-1:
        swap(bx, by, bx+1, by)
    elif event.keysym=='Down' and bx>0:
        swap(bx, by, bx-1, by)
    elif event.keysym=='Right' and by>0:
        swap(bx, by, bx, by-1)
    elif event.keysym=='Left' and by<app.size-1:
        swap(bx, by, bx, by+1)
    
class Application(Frame):
    def __init__(self, master=None, size=3):
        Frame.__init__(self, master)
        self.grid()

        # shuffle numbers
        arr = range(1,size**2)
        random.shuffle(arr)
        arr=[0]+arr

        self.size=size
        self.master.bind_all('<Key>', key)
        self.numbers=[range(size) for x in range(size)]
        self.blankX, self.blankY = 0,0
        
        for i in range(size):
            for j in range(size):
               l = Label(master, 
                            text=arr[size*i+j],
                            font=("Purisa",120),
                            width=2,
                            height=1,
                            fg='White',
                            bg='SteelBlue')
               l.grid(row=i, column=j, padx=5, pady=5)
               self.numbers[i][j]=l
        self.numbers[self.blankX][self.blankX].config(bg='grey', text='')
        

root = Tk()
app = Application(master=root, size=3)
app.mainloop()
