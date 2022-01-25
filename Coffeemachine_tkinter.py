from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
window = Tk()
window.title("Great day coffee shop")
window.geometry('300x400')
lbl = Label(window, text="Welcome:)",font=("Arial Bold", 10))
lbl.grid(column=0, row=0)

def clicked():
    lbl.configure(text="Today's menu",font=("Arial Bold", 10))
    selected = IntVar()
    rad1 = Radiobutton(window,text='Latte--------------$4',value=1, variable=selected)
    rad2 = Radiobutton(window,text='Double Espresso--$6', value=2, variable=selected)
    rad3 = Radiobutton(window,text='Cappocino--------$8', value=3, variable=selected)
    rad4 = Radiobutton(window,text='Coldbrew coffee-$10', value=4, variable=selected)
    rad5 = Radiobutton(window,text='Americano-------$12', value=5, variable=selected)
    lbl1 = Label(text="Everyday is a\ngreat day with\na cup of coffee.",font=("Arial Bold", 10))
    lbl1.grid(column=0, row=2)
    def clicked():
        messagebox.showinfo('Order confirmation!', 'Click Ok for payment.')
        def payment():
           messagebox.showinfo('Payment', 'Please Insert coins..')           
           lbl = Label(window, text='YAY! Coins received.\nPlease take your coffee.',font=("Arial Bold", 10))
           lbl.grid(column=0, row=10)
        payment()    
    btn = Button(window,text='Confirm', command=clicked)
    rad1.grid(column=1, row=1)
    rad2.grid(column=1, row=2)
    rad3.grid(column=1, row=3)
    rad4.grid(column=1, row=4)
    rad5.grid(column=1, row=5)    
    btn.grid(column=1, row=7)
btn = Button(window, text="Go to menu",command=clicked)
btn.grid(column=1, row=0)
window.mainloop()
