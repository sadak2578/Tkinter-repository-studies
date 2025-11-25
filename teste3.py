import tkinter as tk

root = tk.Tk()
root.geometry('620x580')
root.resizable(False, False)


def soma_num():
	
	try:
		num1 = float(numero1.get())
		num2 = float(numero2.get())
		resultado = num1 + num2
		
		if resultado.is_integer():
			resultado = int(resultado)
		
	except ValueError:
		resultado = "Erro: Digite apenas números"
	
	

	#limpa toda a janela
	label1.destroy()
	numero1.destroy()
	label2.destroy()
	numero2.destroy()
	bt_funcao.destroy()
	#expande as colunas para centralizar a mensagem
	root.grid_columnconfigure(0, weight=1)
	resultado_label = tk.Label(root, text=f"O resultado da soma foi: {resultado}")
	resultado_label.grid(row=0, column=0, columnspan=3, sticky="WE")
	

#widegts
#numero um
label1 = tk.Label(root, text='Numero 1:')
label1.grid(row=0, column=0)

numero1 = tk.Entry(root, width=15)
numero1.grid(row=0, column=1)

#numero 2
label2 = tk.Label(root, text='Numero 2:')
label2.grid(row=1, column=0)

numero2 = tk.Entry(root, width=15)
numero2.grid(row=1, column=1)


bt_funcao = tk.Button(root, text='somar',command=soma_num)
bt_funcao.grid(row=2, column=0)





root.mainloop()




