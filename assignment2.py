from tkinter import *
master = Tk(className="User Information")

Label(master, text="What isyour name?").grid(row=1)
Label(master, text="How old are you?").grid(row=3)
Label(master, text="What is your current address?").grid(row=5)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=3, column=1)
e3.grid(row=5, column=1)

mainloop()