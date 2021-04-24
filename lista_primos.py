'''
Criar função que retorna uma lista de primos até n
Recebe um número natural n, com n >= 2, e retorna uma
lista com todos o números primos estritamente menores
que n, em ordem crescente.
'''
def eh_primo(n):

    divs = 0
    for x in range(1, n+1):
        if n % x == 0:
            divs += 1

    if divs == 2:
        return True
    else:
        return False

def lista_primos(n):
    a = []
    cont = 0
    while cont < n:
        validacao_eh_primo = eh_primo(cont)
        if validacao_eh_primo == True:
            a.append(cont)
        cont += 1
    return a
