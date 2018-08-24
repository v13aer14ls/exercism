#!/bin/python3.x
# coding=utf-8
# MANTAINER = Guilherme Amaral
"""
Esse script foi feito para calcular a area de um circulo ou de um triangulo.
A area de um circulo  é  pi vezes o diametro elevado ao quadrado.
A area de um triangulo é a base vezes a altura dividido por 2

"""
print("Iniciando a calculadora...")
opcao = input("Aperte C para Circulo ou T para Triangulo: ")
if opcao == "C":
    raio = float(input("Insira o raio: "))
    area = 3.14159 * raio ** 2
    print("Area: %f" % area)
# ...
elif opcao == "T":
    base = float(input("Insira a Base: "))
    altura = float(input("Insira a Altura: "))
    area = 0.5 * base * altura
    print("Area: %f" % area)
# ...
else:
    print("ERRO! Forma Invalida !")
print("Saindo...")


#Esse script pode ser melhorado se eu criar condicionais caso o camarada ponha strings nas outras inputs.
