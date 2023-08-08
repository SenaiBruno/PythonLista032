'''
Fazer um algoritmo que receba o preço de custo de um produto e mostre como resposta o valor de venda. Sabese que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.
'''

custo = float(input("Informe o custo de compra do produto: "))
acrescimo = float(input("Informe o percentual do acréscimo que o produto receberá antes de ser vendido, em decimal (exemplo: se o valor do percentual é 12%, insira 0.12): "))

venda = (custo * acrescimo) + custo

print(f"O valor foi de R$ {venda:.2f}")