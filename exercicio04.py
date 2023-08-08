"""
Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o programa deverá exibir na
tela o valor do índice de massa corporal desta pessoa (IMC).
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metro
"""
import math

peso = float(input("Seu peso, em quilos: "))
altura = float(input("Sua altura, em metros: "))

imc = peso / math.pow(altura,2)

print(f"Seu IMC é {imc:.2f}")