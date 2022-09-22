###################################################################################
#1. Faça um programa que calcule a raiz quadrada de um número n 
# e trate os casos em que n < 0.
###################################################################################
"""import logging
from typing import Type
import math

logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

def number_validation(n):
    if n < 0: 
        raise ValueError("O número deve ser maior que zero")

def add_number():
    while True:    
        try:
            n = int(input("Insira um número: "))
            number_validation(n)
        except ValueError:
            print("O número deve ser maior que zero")
            logging.error("O número deve ser maior que zero")
            return
        print(math.sqrt(n))  
    
    
add_number()
"""

###############################################################################################
#2. Faça um programa que calcule a divisão de dois números m e n 
# e trate os casos em que n = 0.
###############################################################################################

"""import logging


logging.basicConfig(level=logging.ERROR, filename="logging_users.log")

def validacao_denominador(n):
    if n == 0: 
        raise ZeroDivisionError("Impossível realizar divisão por zero")

def divisao():
    while True:
        try: 
            m = int(input("Insira o numerador: "))
            n = int(input("Insira o denominador: "))
            r = m/n
            validacao_denominador(n)
        except ZeroDivisionError:
            print("Impossível realizar divisão por zero")
            logging.error("Impossível realizar divisão por zero")
            return
        
        print(f"O resultado da divisão é {r}") 

divisao()  """     


###############################################################################################
#3. Observe o programa abaixo:
############################################################################################### 

"""import logging


logging.basicConfig(level=logging.ERROR, filename="logging_users.log")


try: 
    number = int(input("Digite um número: "))
    logging.error(number)
    print(f"O número digitado foi: {number}") 
except ValueError:
    print("Erro nos tipos de dado: deve ser um número")
    logging.error("Erro nos tipos de dado: deve ser um número")"""


###############################################################################################
#4. Tendo em mente que ao executá-lo a exceção NameError é gerada, reescreve o
#código de forma com que tal exceção seja tratada.
###############################################################################################    
"""import logging


logging.basicConfig(level=logging.ERROR, filename="logging_users.log")


try: 
    number = int(input("Digite um número: "))
    logging.info(number)
    print(f"O número digitado foi: {n}") 
except NameError:
    logging.error("Ajustando variável ao valor")
except ValueError:
    print("Erro nos tipos de dado: deve ser um número")
    logging.error("Erro nos tipos de dado: deve ser um número")"""

###############################################################################################
#5. Qual exceção será gerada durante a execução?
############################################################################################### 
"""import math

print(math.sqrt(n)) 

#Erro: NameError -> variável n não foi declarada"""

###############################################################################################
#6. Escreva o que será impresso na tela caso o mesmo seja executado com as 
#seguintes entradas (5, 3):
############################################################################################### 

#A saída impressa será Algo deu errado, pois há divergência entre a declaração de variável e a chamada 
# (result != resultado)

"""try:
    number_1 = float(input("Insira um número: "))
    number_2 = float(input("Insira outro número: "))
    result = number_1/number_2
    
    print("Resultado: {.2f}".format(resultado))
except ValueError:
    print("Isso não é um número")
except ZeroDivisionError:
    print("Divisão por zero indeterminada")
except:
    print("Algo deu errado")"""
            

###############################################################################################
#7. Reescreva o código para que esse erro seja exibido de forma mais clara e amigável.
############################################################################################### 
"""try:
    file = open("file.txt" "r")
    file_lines = file.readline()
    file.close()
except FileNotFoundError:
    print("Arquivo não encontrado")"""
    
    
###############################################################################################
#8. Incremente o código apresentado liberando da memória a referência do arquivo
#tanto nos casos de erro, quanto em execuções bem sucedidas (caso o mesmo fosse
#aberto em modo de escrita).
############################################################################################### 

from asyncore import write


try:
    file = open("file.txt", "w")
    file.write("Exemplo de texto")
except FileNotFoundError:
    print("Arquivo não encontrado")
except IOError:
    print("Não foi possível escrever no arquivo")
finally:
    file.close()
    