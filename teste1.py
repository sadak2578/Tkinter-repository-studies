import tkinter as tk

root = tk.Tk()

root.geometry('690x545')
root.resizable(False, False)

lab1 = tk.Label(root, text='olá mundo!', font=('Arial 12 bold'))
lab1.pack()


root.mainloop()

