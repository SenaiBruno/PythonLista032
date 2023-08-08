'''
Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas
em dias. Obs: Considere os anos com 365 dias e os meses com 30 dias
'''

idadea = int(input("Quantos anos de idade você tem? "))
idadem = int(input("Quantos meses de idade você tem? "))
idaded = int(input("Quantos dias de idade você tem? "))

idade_total = (idadea * 365) + (idadem * 30) + (idaded * 1)

print(f"Você tem {idadea} anos, {idadem} meses e {idaded} de idade.")
print(f"Você tem {idade_total} dias de idade.")