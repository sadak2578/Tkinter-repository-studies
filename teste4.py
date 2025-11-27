import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('780x560')
root.resizable(False, False)
root.columnconfigure(0, weight=1)



img = Image.open("C:\\Users\\Samuel Fernandes\\OneDrive\\Ambiente de Trabalho\\arquivos\\arquivos Python\\Tkinter\\teste4\\foto.jpg")
img = img.resize((200,200))


photo = ImageTk.PhotoImage(img)
label_imagem = tk.Label(root, image=photo)
label_imagem.image = photo
label_imagem.grid(row=0, column=0,  sticky='WE')

label_texto = tk.Label(root, text='a imagem acima mostra o grande papel de parede do mac os', font=('Arial', 9))
label_texto.grid(row=1, column=0, sticky='n', pady=(0,10))

root.mainloop()

