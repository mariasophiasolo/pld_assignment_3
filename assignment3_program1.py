from tkinter import *

window = Tk()
window.title("FIYA'S STORE")
window.minsize(width=500, height=500)
window.configure(background="black")
window.resizable(False,False)

def button_clicked():
    apple_total = int(apple_sb.get()) * 20
    orange_total = int(orange_sb.get()) * 25

    total_bills = apple_total + orange_total
    bills = Label (text= f"Y O U R  T O T A L  B I L L S : ₱{total_bills}", font=("Glacial Indifference", 15), fg="khaki1", bg="black")
    bills.place(x=100, y= 450)

banner = PhotoImage(file="fruitful.png")
banner_label = Label(image=banner,borderwidth=0)
banner_label.place(x=0, y=0)

# Apple (fruit) + Image + Info + Spinbox
apple = PhotoImage(file="apple.png")
apple_label = Label(image=apple, borderwidth=0)
apple_label.place(x=95, y= 280)
apple_price_label = Label(text="2 0  P E S O S", font=("Glacial Indifference", 10), fg="khaki1", bg="black")
apple_price_label.place(x=100, y=390)
apple_sb = Spinbox(window, from_=0, to=100, width=5, fg="dark olive green", bg="black")
apple_sb.place(x=125, y=420)

# Orange (fruit) + Image + Info + Spinbox
orange = PhotoImage(file="orange.png")
orange_label = Label(image=orange, borderwidth=0)
orange_label.place(x=295, y= 280)
orange_price_label = Label(text="2 5  P E S O S", font=("Glacial Indifference", 10), fg="khaki1", bg="black")
orange_price_label.place(x=300, y=390)
orange_sb = Spinbox(window, from_=0, to=100, width=5, fg="dark olive green", bg="black")
orange_sb.place(x=325, y=420)

# Finish button
finish = Button(text="O R D E R", font=("Glacial Indifference", 10, "bold"), fg="khaki1", bg="black", command=button_clicked)
finish.place(x=215, y=450)

window.mainloop()