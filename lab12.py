from dataclasses import dataclass
from decimal import getcontext, Decimal
from recipes_decimal import pi
getcontext().prec = 36
pi = pi()
erro = Decimal(10**(-32))
 
def zeta(s):
    '''Função para calcular a função zeta, conforme pedido.'''
    funcao = 0
    for i in range (1, 101):
        funcao += Decimal(1)/(Decimal(i)**s)
    return funcao
 
def quantidadeAntimateria(p1, p2, p3, p4, x):
    '''Função para determinar o valor de y. Note que as variáveis'''
    '''A, B, C e D foram criadas a fim de simplificar a visualização'''
    '''da função y. '''
 
    A = p1*(Decimal(x).exp())
    B = zeta(p2*x + pi) 
    C = Decimal((-1)*Decimal(p3*x).sqrt()).exp() #Perceba que nas linhas se
                                                 #utilizou o valor de pi 
                                                 #que foi importado.
    D = p4*(2*(pi**3) - x)
    y = (pi + A - B)/(C + D)
    return y
 
def buscaBinaria(dM, p1, p2, p3, p4):
    '''Função para realizar a busca binária e fazer a comparação entre os 2 valores.'''
    '''Note que dM se refere à maior distância'''
 
    esq = Decimal("0.")
    dir = Decimal("50.")
    y = quantidadeAntimateria(p1, p2, p3, p4, Decimal("50."))
    while (abs(esq - dir)) >= erro:
        x = (esq + dir)/2
        y = quantidadeAntimateria(p1, p2, p3, p4, x)
        if abs(y - dM) < erro:
            return x
        if y < dM:
            esq = x
        else:
            dir = x
    return x
 
def entradaParametros():
    '''Função para receber os parâmetros que serão usados na função da antimatéria.'''
 
    p1 = Decimal(input())
    p2 = Decimal(input())
    p3 = Decimal(input())
    p4 = Decimal(input())
    return p1, p2, p3, p4
 
def acharPlaneta(dict):
    '''Essa função retorna o a chave do maior valor presente no dicionário.'''
 
    return max(dict, key = dict.get)
 
def main():
    '''Recebendo os dados até N se igualar a 0, conforme pedido.'''
 
    N = int(input())
    dados = {}
    while N != 0:
        contador = N
        while contador != 0:
            nomePlaneta = input()
            distancia = Decimal(input())
            dados[nomePlaneta] = distancia
            contador -= 1                                                                                                                  
        a, b, c, d = entradaParametros()
        distanciaMaxima = quantidadeAntimateria(a, b, c, d, Decimal("50.")) #Calculando a distância máxima que 
                                                                            #pode ser percorrida.
        dados = {chave:valor for chave, valor in dados.items() if valor < distanciaMaxima} 
        #Acima, foi utilizado o conhecimento em estrutura de dados para retirar os pares c
        if dados != {}:
            planetaEscolhido = acharPlaneta(dados)
            maiorDistancia = dados[planetaEscolhido] #Acha-se a maior distância a partir da chave.
            combustivel = buscaBinaria(maiorDistancia, a, b, c, d) #Determina o combustível gasto
                                                                #utilizando a busca binária.
            print(planetaEscolhido)
            print(f"{combustivel:.28f}")
        else:
                print("GRAU~~")
        N = int(input())
        dados = {}
 
if __name__ == '__main__':
    main()
