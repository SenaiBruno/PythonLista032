"""
Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
"""

pesokg = int(input("Seu peso:"))
alturam = int(input("Sua altura:"))

pesog = pesokg * 1000
alturacm = alturam * 100

print("Seu peso em gramas é:", pesog, "e sua altura em centimetros é:", alturacm)