'''
Criar função que verifica se um número é quase de Armstrong
Recebe um número natural n, com n >= 0, e retorna
verdadeiro se n atende aos seguintes critérios:
1) não ser um número de Armstrong;
2) o resultado da soma de seus digitos elevados ao número total
de digitos é igual a ele próprio somado ou subtraído de 1.
'''

def eh_quase_armstrong(n):
    soma = 0  
    temp = n  
    qtd = str(n)
    while temp > 0:  
        digito = temp % 10  
        soma += digito ** len(qtd)
        temp //= 10  
    if soma == n-1 or soma == n+1:
        return True
    else:
        return False