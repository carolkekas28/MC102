def recebeMatriz(n):
    '''Função simples para receber os elementos da matriz.'''
 
    m = []
    for i in range(n):
        m.append(input().split())
    for i in range(n):
        for j in range(n):
            m[i][j] = int(m[i][j])
    return m    
 
def cofator(M, i, j):
    '''Função que devolve o cofator da matriz.'''
 
    return [x[:j] + x[j+1:] for x in (M[:i] + M[i+1:])]
 
def calculaDeterminante(M):
    '''Função para calcular recursivamente o determinante.'''
    '''Det(M) = (-1)**(i+j)*elemento*det(cofator)'''
 
    if len(M) == 2: #Caso mais simples, onde se trabalha apenas com uma matriz 2x2. 
        det = M[0][0]*M[1][1] - M[1][0]*M[0][1]
        return det
    else:
        det = 0
        #Para a resolução do lab, é possível trabalhar com qualquer linha i desejada.
        for j in range(len(M)):
            #Caso em que a linha i = 0.
            sinal = (-1)**(j)
            sub_det = calculaDeterminante(cofator(M, 0, j))
            det += sinal*M[0][j]*sub_det
    return det
 
def main():
    m = int(input())
    N = int(input())
    produtoDeterminantes = 1
    for i in range (m):
        matriz = recebeMatriz(N)
        determinante = calculaDeterminante(matriz)
        produtoDeterminantes *= determinante
    print("Após as", m, "transformações, o objeto", N, end = '-')
    print("dimensional teve o volume multiplicado no valor", produtoDeterminantes, end = ".")
 
if __name__ == '__main__':
    main()
