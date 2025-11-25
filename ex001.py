#Atribuir valores as variáveis A,B,C,D 
#Atribuindo os valores a todas as variáveis em uma só linha pq to com preguiça de escrever em mais linhas
A,B,C,D = 2, 3, 4, 0

print(f'O valor de A é: {A}')
print(f'O valor de B é: {B}')
print(f'O valor de C é: {C}')
print(f'O valor de D é: {D}')

#Troque o valor da variável C para um valor acrecido de 1
C = C + 2
print('-=' * 20)
print(f'O valor da variável C agora é: {C}')
#Atribuir o valor A a soma de  A com o valor atual de C
D = A + C
print(f'O novo valor de D é: {D}')
