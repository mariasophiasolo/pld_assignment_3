import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("FIYA'S STORE")
window.minsize(width=500, height=500)
window.configure(background="black")
window.resizable(False,False)

def calculate_apples():
    money = int(money_entry.get())
    apple_price = int(apple_price_entry.get())
    max_apples = int(money // apple_price)

    remaining_money = money % apple_price
    result_message = tk.Label(text=f"__________\n\nWith ₱ {money}, you can buy {max_apples} apple.\nAfter buying {max_apples} apple,\nyou will have ₱{remaining_money:.2f} remaining.\n__________", font=("Times New Roman", 10, "bold"), fg="khaki1", bg="black")
    result_message.place(x=285, y=390)

# Store banner
banner = tk.PhotoImage(file="fruitful.png")
banner_label = tk.Label(image=banner,borderwidth=0)
banner_label.place(x=0, y=0)

# Apple Image
apple = tk.PhotoImage(file="apple.png")
apple_label = tk.Label(image=apple,borderwidth=0)
apple_label.place(x=325, y=290)

# Money amount entry
money_label = tk.Label(window, text="E N T E R  T H E  A M O U N T  O F  Y O U R  M O N E Y: ₱", bg="black", fg="khaki1", font=("Glacial Indifference", 9))
money_label.place(x=20, y=280)
money_entry = tk.Entry(window)
money_entry.place(x=25, y=310)

# Apple price entry
apple_price_label = tk.Label(window, text="E N T E R  T H E  P R I C E  O F  A P P L E: ₱", bg="black", fg="khaki1", font=("Glacial Indifference", 9))
apple_price_label.place(x=20, y=350)
apple_price_entry = tk.Entry(window)
apple_price_entry.place(x=25, y=380)

# Calculate
calculate_button = tk.Button(window, text="O R D E R", font=("Glacial Indifference", 10, "bold"), fg="khaki1", bg="black", command=calculate_apples)
calculate_button.place(x=25, y=430)

window.mainloop()