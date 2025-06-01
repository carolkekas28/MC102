dia_mes = int(input())
dia_semana = str(input()) 
valor_compra = float(input())
 
if (dia_mes%7 == 0):
    valor_final = valor_compra*0.5
else: 
    if (dia_semana == 'sexta-feira'):
        valor_final = valor_compra*0.75
    else:
        valor_final = valor_compra - dia_mes
 
#Como não é possível obter um valor final negativo, devemos tomar cuidado para que isso não ocorra.
if(valor_final >= 0):
    print(f'{valor_final:,.2f}')
else:
    print("0.00")
#Aqui, iremos definir qual mensagem será exibida no fim do programa. 
if (dia_semana == 'segunda-feira'):
    print("É um dia terrível, você não devia ter saído da cama.")
else: 
    if (dia_semana == 'sábado') or (dia_semana == 'domingo'):
        print("Agradecemos a preferência, tenha um ótimo fim de semana!")
    else:
        print("Agradecemos a preferência, tenha uma ótima", dia_semana, end = "!")
