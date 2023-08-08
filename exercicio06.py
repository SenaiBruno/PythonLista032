'''
Fazer um algoritmo que pergunte o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por
ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas,
exibir ao final o seu nome, o salário fixo, a comissão e o salário completo (fixo + comissão sobre vendas) no final
do mês.
'''

nome = input("Qual o seu nome: ")
salarioc = float(input("Qual seu salário: "))
vendas = float(input("Qual o total de vendas feitas por você no mês, em dinheiro: "))

comissao = vendas * 0.15
salario = comissao + salario

print(f"Seu nome: {nome}")
print(f"Seu salário fixo: R$ {salario:.2f}")
print(f"Valor de sua comissão: R$ {comissao:.2f}")
print(f"Salário completo: R$ {salarioc:.2f}")
