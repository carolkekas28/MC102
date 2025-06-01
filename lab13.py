pastas = {} 
def renomeia(chave, texto): 
    #Devolve recursivamente as linhas de texto que vão ser impressas. 
    if chave in pastas: 
        return renomeia(pastas[chave], texto) + "_" + chave 
    else: 
        return texto 
  
def mostraDados(l): 
    for i in range (len(l)): 
        print(l[i]) #Função pra imprimir os elementos da lista. 
  
def entrada(): 
    #Recebe os itens de entrada (no caso, a pasta-raiz e a quantidade 
    #n de subpastas que vão ser criadas). 
    arquivos = [] 
    pasta_raiz, n = input().split() 
    for i in range (int(n)): 
        nome = input().split() 
        pastas[nome[0]] = nome[1] #Aqui, são adicionadas as subpastas ao dicionário criado anteriromente. 
        arquivos.append(renomeia(nome[0], pasta_raiz)) 
    mostraDados(arquivos) 
  
def main(): 
    entrada() 
  
if __name__ == '__main__': 
    main() 
