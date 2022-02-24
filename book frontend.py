from tkinter import *
import backend

window = Tk()

#=========================label========================
l1 = Label(window, text = 'book name: ')
l1.grid(row = 0 , column = 0)

l2 = Label(window, text = 'Auor: ')
l2.grid(row = 0 , column =2)

l3 = Label(window, text = 'Year: ')
l3.grid(row = 1 , column = 0)

l4 = Label(window, text = 'serial number : ')
l4.grid(row = 1 , column = 2)

#=========================enteris========================

book = StringVar()
l1_entery = Entry(window,textvariable = book,  width = 15,)
l1_entery.grid(row = 0 , column = 1)

Autor = StringVar()
l2_entery = Entry(window,textvariable = Autor,  width = 15)
l2_entery.grid(row = 0 , column = 3)

year = StringVar()
l3_entery = Entry(window,textvariable= year,  width = 15)
l3_entery.grid(row = 1 , column = 1)

serial = StringVar()
l4_entery = Entry(window,textvariable = serial,  width = 15)
l4_entery.grid(row = 1 , column = 3)

list1 = Listbox(window, width = 35, height = 10)
list1.grid(row =3,column = 0, rowspan= 6 , columnspan = 2, padx = 5 , pady = 5)
sc = Scrollbar(window)
sc.grid(row = 3 , column = 2, rowspan = 6 )

#=========================buttons========================
b1 = Button(window , text = 'view all', width = 12)
b1.grid(row = 2 , column = 3, padx = 2 , pady = 1)

b2 = Button(window , text = 'search', width = 12)
b2.grid(row = 3 , column = 3, padx = 2 , pady = 1)

b3 = Button(window , text = 'update', width = 12)
b3.grid(row = 4 , column = 3, padx = 2 , pady = 1)

b3 = Button(window , text = 'delete', width = 12)
b3.grid(row = 5 , column = 3, padx = 2 , pady = 1)

b5 = Button(window , text = 'close', width = 12)
b5.grid(row = 6  , column = 3, padx = 2 , pady = 1)

window.mainloop()