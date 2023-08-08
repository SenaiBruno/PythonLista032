"""
Fazer um algoritmo que pergunte dois números e ao final apresente os seguintes valores: a soma dos dois
números, a subtração do primeiro pelo segundo número, a subtração do segundo pelo primeiro número, a
multiplicação entre os dois números, a divisão do primeiro pelo segundo número, e também o resto da divisão
do primeiro pelo segundo número.
"""


num1 = int(input("Escolha o seu primeiro número:"))
num2 = int(input("Escolha o seu primeiro número:"))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print("Soma:", soma)
print("Subtração:", sub)
print("Multiplicação:", mult)
print("Divisão:", div)

