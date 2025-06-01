import locale

quantidade = int(input())
taxa_vibranium = float(input())
constante_solv = int(input())
constante_prog = int(input())
soma_parcial = 0
multiplicador = 0
soma_total = 0
progressao = 0
m = 0
 
#Primeiro, vamos calcular e mostrar os valores referentes à soma parcial e à soma total.
for i in range (1,quantidade+1):
    print(i, end = " ")
    multiplicador = constante_solv + i
    soma_parcial = taxa_vibranium*multiplicador
    soma_total += soma_parcial
    print(str(f'{soma_parcial:,.2f}').replace(",", ""), end = " ") 
    print(str(f'{soma_total:,.2f}').replace(",", "")) 
print(str(f'{soma_total:,.2f}').replace(",", "")) 
 
#Agora, vamos calcular os valores da progressão aritmética que serão menores do que a soma total.
while (progressao <= soma_total):
    m += 1
    progressao += constante_prog 
    if(progressao <= soma_total):
        print(progressao)
print(m-1)
print("BATERIA DE TESTES TERMINADA")
