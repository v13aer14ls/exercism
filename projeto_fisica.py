#!/usr/bin/env python
#Mantainer = Guilherme Amaral
"""
Mais um exercicio chato que calcula ai uma conversão de Celsius pra Fahrenheit e umas outras coisas de fisica
"""

train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp
f100_in_celsius = f_to_c(100)

def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

print(f100_in_celsius)
print(c0_in_fahrenheit)

def get_force(mass,acceleration):
  return mass * acceleration
train_force = get_force(train_mass,train_acceleration)
print (train_force)

print ("The GE train supplies %s Newtons of force" % train_force)

def get_energy(mass,c):
  c = 3*10**8
  return mass * c**2
bomb_energy =  get_energy(bomb_mass,1)
print("A 1kg bomb supplies %s Joules." % bomb_energy)

def get_work(mass,acceleration,distance):
  force = get_force(mass,acceleration) * distance
  return force
train_work =  get_work(train_mass,train_acceleration,train_distance)
print ("A GE train does %s Joules of work over %s meters." % (train_work , train_distance))
