'''
Criar uma função que verifica se um número é primo
Recebe um número natural n, com n >= 2, e retorna verdadeiro se
n é um número primo e falso caso contrário.
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