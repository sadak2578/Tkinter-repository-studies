import tkinter as tk
from PIL import Image, ImageTk




root = tk.Tk()
root.geometry('780x560')
root.resizable(False, False)
root.columnconfigure(0, weight=1)

def somatoria():
	pass

def mensagem_credito():
	pass

img = Image.open('C:\\Users\\Samuel Fernandes\\OneDrive\\Ambiente de Trabalho\\arquivos\\arquivos Python\\Tkinter\\teste5\\function-mathematical-symbol-svgrepo-com.png')
img = img.resize((80,80))

logo = ImageTk.PhotoImage(img)

label_logo = tk.Label(root, image=logo)
label_logo.image = logo
label_logo.grid(row=0, column=0, sticky='WE')


bt1 = tk.Button(root, text='Somar', command=somatoria)
bt1.grid(row=1, column=0, sticky='w', padx=70 ,pady=(30,70))





bt_credito = tk.Button(root, text='Crédito', command=mensagem_credito)
bt_credito.grid(row=1, column=0, sticky='e', padx=70, pady=(30,70))




root.mainloop()