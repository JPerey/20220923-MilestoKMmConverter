from tkinter import *

# window

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=250, height=150)
window.config(padx=10, pady=40)


# functions

def change_label():
    user_input = int(entry1.get())
    km_result = round(user_input * 1.609, 2)
    label3.config(text=km_result)


# WIDGETS

entry1 = Entry()
entry1.grid(column=1, row=0)

button1 = Button(text="Calculate", command=change_label)
button1.grid(column=1, row=2)

label1 = Label(text="Miles")
label2 = Label(text="is equal to")
label3 = Label(text="0")
label4 = Label(text="Km")
label1.grid(column=2, row=0)
label2.grid(column=0, row=1)
label3.grid(column=1, row=1)
label4.grid(column=2, row=1)

window.mainloop()
