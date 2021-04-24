'''
Criar função que conta a quantidade de primos em uma sequẽncia
Recebe uma sequência de números naturais s e retorna
um dicionário com a contagem de ocorrências de cada número
primo da sequência. Números não primos devem ser ignorados.
Os números da sequência serão sempre maiores ou iguais a 2.
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

def conta_primos(s):
    dic = {}
    for numero in s:
        validacao_eh_primo = eh_primo(numero)
        if validacao_eh_primo == True:
            if numero not in dic:
                dic[numero] = 1
            else:
                dic[numero] += 1
    return dic