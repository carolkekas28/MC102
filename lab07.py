def remove_ultimo_elemento(l):
#Função criada para garantir que o termo adicionado após "/" será retirado do último elemento da lista. 
    elemento_final = l[-1]
    for i in range (len(elemento_final)):
        if elemento_final[i] == '/':
            l[-1] = elemento_final[0:i] #Com isso, apaga-se de l[-1] o termo que deseja ser retirado da lista.
    return l[-1]
 
def achar_elemento_pra_retirar(l):
#O nome é autoexplicativo. Função pra retirar o elemento digitado incorretamente por Peter.
    elemento_final = l[-1]
    str = []
    num = 0
    for i in range (len(elemento_final)):
        if elemento_final[i] == '/':
            num = i
    for i in range (num + 2, len(elemento_final)):
        str.append(elemento_final[i])
    return str
 
def remove_repetidos_e_ordena(l):
#Função criada para remover os elementos repetidos da lista que é dada pelo usuário.
    l_novo = []
    for x in l:
        if x not in l_novo:
            l_novo.append(x) #Como a lista é vazia, automaticamente ela adiciona o primeiro elemento de l. Após isso,
                             #um novo elemento só será adicionado se ele já não estava na lista antes.
    l_novo.sort() #A função sort é utilizada apenas para ordenar os elementos da nova lista.
    return l_novo
 
def apenas_remove_repetidos(l):
#Essa função apenas remove os elementos repetidos da lista, sem ordená-los. Ela é importante para
#garantir que os elementos de cada categoria serão posteriormente mostrados na ordem certa. 
    l_novo = []
    for x in l:
        if x not in l_novo:
            l_novo.append(x)
    return l_novo
 
def contando_ocorrencias(l1, l2):
#Função para contar a quantidade máxima de vezes que um elemento apareceu sequencialmente.
    l = [0]*len(l2)
    for i in range(len(l2)):
        for j in range(1, len(l1)):
            if l2[i] == l1[j-1] and l2[i] == l1[j]: #Aqui, se o elemento anterior for igual ao seguinte, soma-se 1 à lista de frequências.
                l[i] += 1
        if l[i] != 0:
            l[i] = l[i] + 1 #Apenas tomando cuidado para contabilizar o último elemento que aparece em sequência.
    return l
 
def ajeita_formato(l):
#Vamos trocar os espaços por "-" e as letras maiúsculas por minúsculas, conforme foi pedido.
    l = l[0:2] + l[2:len(l)].lower() #Para as letras que não correspondem à categoria da foto, usamos a função lower() para torná-las minúsculas.
    l = l.replace(" ", "-") #Alterando os espaços para "-", conforme havia sido pedido.
    return l
 
if __name__ == "__main__":
    lista = []
    lista = input().split(", ")
    #Vamos agora encontrar qual elemento deverá ser removido da lista.
    termo = achar_elemento_pra_retirar(lista)
    termo = "".join(termo) #Do jeito que havíamos feito, iríamos obter uma lista, e não uma string usual.
    #Nessa parte do código, vamos retirar uma parte do elemento lista[-1], que corresponde ao termo errado.
    lista[-1] = remove_ultimo_elemento(lista)
    #Agora, vamos criar uma lista que irá conter os termos da lista anterior, mas sem repetições.
    lista_ordenada = remove_repetidos_e_ordena(lista) #Precisamos da lista ordenada para contar as frequências!
    frequencias = contando_ocorrencias(lista, lista_ordenada)
    for i in range (len(frequencias)):
        if frequencias[i] == max(frequencias):
            mais_repetido = lista_ordenada[i]
    #Como a posição do elemento é a mesma da sua frequência, basta
    #determinar qual elemento da lista de frequências é máximo.
    print(mais_repetido, max(frequencias))
    print(len(lista_ordenada))
    lista = list(filter(lambda x: x!= termo, lista))
    lista_desordenada = apenas_remove_repetidos(lista)
    for i in range (len(lista_desordenada)):
        lista_desordenada[i] = ajeita_formato(lista_desordenada[i])
    #Agora, vamos criar três listas referentes às categorias das fotos.
    HA = []
    CR = []
    CC = []
    for i in range (len(lista_desordenada)):
        termo = lista_desordenada[i]
        if termo[0:2] == "HA":
            HA.append(termo)
        elif termo[0:2] == "CC":
            CC.append(termo)
        elif termo[0:2] == "CR":
            CR.append(termo)
    print(HA)
    print(CR)
    print(CC)
