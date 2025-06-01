#Primeiro, vamos criar a função para gerar o número pseudo-aleatório.
def numero_aleatorio(x):
    return ((7*x + 111)%1024)
#Agora, cria-se uma função para verificar se o jogo deve ou não ser encerrado.
def checagem (vS, vC):
    if vS <= 0:
        print("Sarah foi derrotada...")
        exit()
    elif vC <= 0:
        print("O clone foi derrotado! Sarah venceu!")
        print("FIM - PARABENS")
        exit()
#A primeira habilidade, o soco, vai necessitar de 6 parâmetros para calcular o dano recebido.
#Note que aS, dS, vS se referem à Sarah, enquanto aC, dC, vC, ao clone. Isso será utilizado posteriormente.
def soco(cont1, semente1, aS1, dS1, aC1, dC1):
    m = semente1%3
    if cont1%2 == 0:
        soco = (aS1 - dC1)*m
        if (soco <= 0):
            soco = 0
    elif cont1%2 == 1:
        soco = (aC1 - dS1)*m
        if (soco <= 0):
            soco = 0
    return soco
 #Determinando o valor do dano ao ser utilizada a habilidade da faca.
def arremesso_de_facas (cont2, semente2, aS2, aC2):
    n = semente2%6
    arremesso_de_facas = 0
    #Cuidando para que n não seja igual a 1!
    if n != 1:
        for j in range (1, n+1): 
            if (cont2%2 == 0): 
                arremesso_de_facas = arremesso_de_facas + aS2//(3**j) 
            elif (cont2%2 == 1): 
                arremesso_de_facas = arremesso_de_facas + aC2//(3**j) 
    #Caso em que n é 1. 
    elif n == 1:
        if (cont2%2 == 0):
            arremesso_de_facas = aS2//3
        elif (cont2%2 == 1):
            arremesso_de_facas = aC2//3
    return arremesso_de_facas
 
#Na invocação da fada, iremos gerar os dois números pseudo-aleatórios p e q, então essa função retorna 2 valores.
def invocacao_de_fada (semente3, p3, q3):
    p3 = semente3%100
    semente3 = numero_aleatorio(semente3)
    q3 = semente3%1024
    print("MENSAGEM DEBUG - número gerado:", q3)
    return p3, q3
    
 
lista_acoes = []
dano = 0
P = 1
Q = 1
acao = 'a'
vidaSarah, ataqueSarah, defesaSarah = input().split()
vidaSarah = int(vidaSarah)
ataqueSarah = int(ataqueSarah)
defesaSarah = int(defesaSarah)
vidaClone, ataqueClone, defesaClone = input().split()
vidaClone = int(vidaClone)
ataqueClone = int(ataqueClone)
defesaClone = int(defesaClone)
semente = int(input())
try:
    while (acao != ''):
        acao = str(input())
        if (acao != ''): 
            lista_acoes.append(acao)
except EOFError as e:
    print(end = "")
#Vamos dar início ao jogo.
for i in range (0, len(lista_acoes)):
    semente = numero_aleatorio(semente)
    print("MENSAGEM DEBUG - número gerado:", semente)
 
    if lista_acoes[i] == 'soco':
        dano = soco(i, semente, ataqueSarah, defesaSarah, ataqueClone, defesaClone)
        if i%2 == 0:
            print("O clone sofreu", dano, "pontos de dano!")
            vidaClone = vidaClone - dano
        else:
            print("Sarah sofreu", dano, "pontos de dano!")
            vidaSarah = vidaSarah - dano
        checagem(vidaSarah, vidaClone)
    
    elif lista_acoes[i] == 'facas':
        dano = arremesso_de_facas(i, semente, ataqueSarah, ataqueClone)
        if i%2 == 0:
            print("O clone sofreu", dano, "pontos de dano!")
            vidaClone = vidaClone - dano
        else:
            print("Sarah sofreu", dano, "pontos de dano!")
            vidaSarah = vidaSarah - dano
        checagem(vidaSarah, vidaClone)
    
    elif lista_acoes[i] == 'fada':
        p, q = invocacao_de_fada(semente, P, Q)
        #Agora, vamos lidar com o que ocorre para os diferentes valores de q. 
        if q%2 == 1 and q < 100:
            if i%2 == 0:
                vidaSarah = vidaSarah + p
                ataqueSarah = ataqueSarah + q
                print("Sarah ganhou", p, "pontos de vida!")
                print("Sarah ganhou", q, "pontos de ataque!")
            if i%2 == 1:
                vidaClone = vidaClone + p
                ataqueClone = ataqueClone + q
                print("O clone ganhou", p, "pontos de vida!")
                print("O clone ganhou", q, "pontos de ataque!") 
        elif q%2 == 0 and q < 100 and q != 0:
            if i%2 == 0:
                vidaSarah = vidaSarah + p
                defesaSarah = defesaSarah + q
                print("Sarah ganhou", p, "pontos de vida!")
                print("Sarah ganhou", q, "pontos de defesa!")
            elif i%2 == 1:
                vidaClone = vidaClone + p
                defesaClone = defesaClone + q
                print("O clone ganhou", p, "pontos de vida!")
                print("O clone ganhou", q, "pontos de defesa!")
        elif q >= 1019:
            if i%2 == 0:
                print("Sarah ganhou", p, "pontos de vida!")
                print("O quê? A fada trouxe um monstro gigante com ela!")
                print("O Clone e o castelo foram destruídos,")
                print("e Sarah agora tem um novo pet.")
                print("FINAL SECRETO - PARABENS???")
                exit()
            elif i%2 == 1:
                print("O clone ganhou", p, "pontos de vida!")
                print("O quê? A fada trouxe um monstro gigante com ela!")
                print("Sarah foi derrotada...")
                exit()
        else:
            if i%2 == 0:
                vidaSarah = vidaSarah + p
                print("Sarah ganhou", p, "pontos de vida!")
            elif i%2 == 1:
                vidaClone = vidaClone + p
                print("O clone ganhou", p, "pontos de vida!")
        #Tomando o cuidado para que a semente mude de valor 2 vezes ao utilizar essa função!
        semente = numero_aleatorio(semente)
        p = 1 
        q = 1
