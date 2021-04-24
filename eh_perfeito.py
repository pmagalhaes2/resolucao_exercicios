'''
Função que verifica se um número é dito perfeito
Recebe um número natural n, com n >= 2, e retorna verdadeiro se
n é dito um número perfeito e falso caso contrário.
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
