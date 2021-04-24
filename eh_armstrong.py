'''
Criar função que verifica se um número é de Armstrong
Recebe um número natural n, com n >= 0, e retorna
verdadeiro se n é um número de Armstrong e falso
caso contrário.
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