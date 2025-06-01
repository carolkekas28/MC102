ista_operacoes = [] 
lista_a = [] 
lista_b = [] 
operacao = 'b'
a = 1 
b = 1 
operacao = str(operacao) 
a = int(a) 
b = int(b) 
 
while (operacao != '0'):
    operacao, a, b = input().split(" ")
    if (operacao != 0):
        lista_operacoes.append(operacao)
        lista_a.append(int(a))
        lista_b.append(int(b))
lista_operacoes.remove('0')
 
for i in range (0, len(lista_operacoes)):
    if (lista_operacoes[i] == '+'):
        print(lista_a[i] + lista_b[i])
    elif (lista_operacoes[i] == '-'):
        print(lista_a[i] - lista_b[i])
    elif (lista_operacoes[i] == '*'):
        print(lista_a[i]*lista_b[i])
    elif(lista_operacoes[i] == '/'):
        print(lista_a[i]//lista_b[i], end = " ") 
        print(lista_a[i]%lista_b[i]) 
    elif(lista_operacoes[i] == ';'):
        if (lista_a[i] > lista_b[i]):
            for j in range (1, (lista_a[i] - lista_b[i])+1):
                if ((lista_a[i] - lista_b[i])%j == 0):
                    if (j < lista_a[i] - lista_b[i]):
                        print(j, end = " ")
                    else:
                        print(j)
        elif (lista_b[i] > lista_a[i]):
            for j in range (1, (lista_b[i] - lista_a[i])+1):
                if ((lista_b[i] - lista_a[i])%j == 0):
                    if (j < lista_b[i] - lista_a[i]):
                        print(j, end = " ")
                    else:
                        print(j)
        elif (lista_b[i] == lista_a[i]):
            print(0)
