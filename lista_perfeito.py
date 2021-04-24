'''
Função que lista os números ditos perfeitos até n
Recebe um número natural n, com n >= 2, e retorna uma lista
com todos os números perfeitos estritamente menores que n,
em ordem crescente.
'''
def eh_perfeito(n):
    if n >= 2:
        soma_divs = 0
        for div in range(1, n):
            if n % div == 0:
                print(div)
                soma_divs = soma_divs + div
        if soma_divs == n:
            return True
        else:
            return False

def lista_perfeitos(n):
    if n >= 2:
        lista = []
        i = 1
        while i < n:
            resposta = eh_perfeito(i)
            if resposta == True:
                lista.append(i)
            i += 1
        return lista
