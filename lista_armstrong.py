'''
Criar função que lista os números e Armstrong até n
Recebe um número natural n e retorna uma lista com todos o
números de Armstrong estritamente menores que n, em ordem
crescente.
'''

def eh_armstrong(n):
    if n >= 0:
        soma = 0  
        temp = n
        qtd = str(n)
        while temp > 0:  
            digito = temp % 10  
            soma += digito ** len(qtd) 
            temp //= 10  
      
        if n == soma:  
            return True
        else:  
            return False 

def lista_armstrong(n):
    lista = []
    i = 0
    while i < n:
        resposta = eh_armstrong(i)
        if resposta == True:
            lista.append(i)
        i += 1
    return lista