#!/bin/python3x
#Mantainer Guilherme Amaral
"""
Esse aqui eu não vou nem me dar o trabalho de traduzir de tão chato.
"""

"""
This program generates
passages that are generated
in mad-lib format
Author: Katherin
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."
# ...
print ("Mad Libs has started !")
# ...
name = input("Enter a name: ")
a1 = input("Enter an adjective: ")
a2 = input("Enter another adjective: ")
a3 = input("Enter the last adjective: ")
verb = input("Enter a Verb: ")
noun1 = input("Enter the first noun: ")
noun2 = input("Enter the second noun: ")
animal = input("Enter an animal: ")
food = input("Enter a food: ")
fruit = input("Enter a fruit: ")
superhero = input("Enter a superhero: ")
country = input("Enter a country: ")
dessert = input("Enter a dessert: ")
year = input("Enter a year: ")

# ...
print (STORY) % (name, a1, a2, animal, food, verb, noun1, fruit, a3, name, superhero, name, country, name, dessert, name, year, noun2)
#consertar esse final cagado aqui 
