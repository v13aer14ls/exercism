#!/bin/Python3.x
#Mantainer= Guilherme

#O piglatim remove a primeira letra de uma palavra envia ela para o final da mesma e adicona o sufixo "ay" ao final da palavra
#Seja la quem inventou isso provavelmente tinha muito tempo livre

pyg = "ay"
palavra=input("Insira uma palavra: ")
if len(palavra) > 0 and palavra.isalpha():
	palavra_mudada = palavra.lower()
	letra = palavra_mudada[0]
	palavra_nova = palavra_mudada[1:] + letra + pyg

	print(palavra_nova)
else:
	print ("Nica Nica")
