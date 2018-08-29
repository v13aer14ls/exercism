#!/bin/python2.x/env
#Mantainer Guilherme

#Script de um exercicio sobre pizza ! Eu adoro pizza.


toppings = ['pepperoni', 'pineapple','cheese','sausage', 'olives', 'anchovies','mushrooms']
prices = [2 , 6 ,1 ,3 ,2 , 7, 2]
num_pizzas = len(toppings)
print (("we sell %s kinds of pizza !") % num_pizzas)

pizzas = list(zip(prices,toppings))
print (list(pizzas))
pizzas.sort()
cheapest_pizza = pizzas[0]
#A man in a business suit walks in and shouts "I will have your MOST EXPENSIVE pizza!"
priciest_pizza = pizzas[-1:]
three_cheapest = pizzas[:3]
print (three_cheapest)
num_two_dollar_slices = pizzas.count("2")
