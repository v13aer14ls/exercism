#!/bin/python2/env
#Guilherme Amaral

#Mais um exercicio daqueles 


hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2, 1]

#1. Create a variable total_price, and set it to 0.
total_price = 0
#2. Iterate through the prices list and add each price to the variable total_price.

for price in prices:
  total_price += price

print(total_price)

# 3. create a variable called average_price that is the total_price divided by the number of haircuts.
average_price = total_price/len(hairstyles)

#4. prtint average price string
print("Average Price: " + str(average_price))

#5. Create list comprehension to make a list titled new_prices, with each element subtracted by 5

new_prices = [price - 5 for price in prices]
#6. Print new prices
print(new_prices)

#7. create new variable called total_revenue and set it equal to 0

total_revenue = 0

#8. create a loop that goes from 0 to len(hairstyles)-1

for i in range(len(hairstyles)-1):
  print(i)
#9 Add the product of prices[i] (the price of the haircut at position i) and last_week[i]

for i in range(0, len(hairstyles)-1):
  total_revenue += prices[i] * last_week[i]
#print total revenue
print(total_revenue)

#find average daily revenue
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

#12. create comprehension list for haircuts less than 30
cuts_under_30 = list(zip(hairstyles,[price for price in new_prices if price < 30]))
print(list(cuts_under_30))
