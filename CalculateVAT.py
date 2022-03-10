

# expressão lógica  =>  Expressão que produz verdadeiro ou falso 
#                       (True ou False). 
#
# condição          =>  Expressão lógica no contexto de uma decisão (ou
#                       de um ciclo)
#
# bloco de instruções   =>  conjunto de instruções delimitado de alguma 
#                           forma. Em Python, essa delimitação é feita
#                           pela indentação. Noutras linguagens, é feita,
#                           através de palavras-reservadas, ou de caracteres 
#                           específicos (exemplo: { })
#
# decisão           =>  Instrução composta que permite executar um bloco
#                       de instruções mediante o resultado de condição.
#                       Em Python, só existe um tipo de decisão: a
#                       instrução IF. Em Java/C/C++/C/JavaScript/, além da
#                       instrução IF, temos também a instrução SWITCH-CASE.
#                       As instruções de decisão são também designadas
#                       de selecção.
#
# IF em PYTHON      =>
#   | if CONDIÇÃO:
#   |     INST_1
#   |     INST_2
#   |     ....
#   |     INST_N
#   | else:
#   |     INST_ALT_1
#   |     INST_ALT_2
#   |     ...
#   |     INST_ALT_M
#
# Também existe a cláusula ELIF que abordaremos noutro exemplo

# $ python3 calculo_iva2.py 100 23 10
#   O preço final é 110.70
# $

import sys
from decimal import Decimal as dec

if len(sys.argv) not in (3, 4):
    print(f"Utilização: python[3] {sys.argv[0]} PRECO TAXA_IVA [DESCONTO]")
    sys.exit(2)

preco = dec(sys.argv[1])
taxa_iva = dec(sys.argv[2])
desconto = dec(0 if len(sys.argv) == 3 else sys.argv[3])

preco_final = preco * (1 + taxa_iva/100) * (1 - desconto/100)

print(f"O preço final é {preco_final:.2f}")



# if len(sys.argv) == 3: 
#     desconto = dec(0)
# else:
#     desconto = dec(sys.argv[3])

# desconto = dec(0)
# if len(sys.argv) == 4:
#     desconto = dec(sys.argv[3])

# EXPRESSÃO CONDICIONAL/IF:
#
#       EXPR1 if CONDICAO else EXPR2
#
# x = 5
# if x > 10:
#      y = 200
#  else:
#      y = 50

# y = 200 if x > 10 else 50