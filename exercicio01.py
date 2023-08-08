"""
Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
"""

conta = float(input("Valor conta a ser paga: "))
acrescimo = (conta * 0.10) + conta

print("Valor com o acréscimo dos 10%: ", acrescimo)