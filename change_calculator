## I, Allyson Sousa Pereira, Student ID: 000851700, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
## Assignment 2, Question 2

import random
from math import floor
from webbrowser import get

def getDollars(value):
  return floor(value)

def getQuarters(value):
  quarters = 0
  while value >= 0.25:
    value -= 0.25
    quarters += 1
  return quarters


def getDimes(value):
  dimes = 0
  while value >= 0.10:
    value -= 0.10
    dimes += 1
  return dimes

def getNickels(value):
  nickels = 0
  while value >= 0.05:
    value -= 0.05
    nickels += 1
  if value > 0:
    nickels += 1
  return nickels


# CALCULATE amount of transaction AS amount
amount = random.randint(0,20) + round (random.randint(0,100)/100,2)
#amount = 0.2

# SHOW amount to screen
print("The price to be paid is: {}" .format(amount))

# GET amount of payment FROM keyboard AS payment
payment = float(input("Insert the amount of money for the payment: "))
# ASSUME payment >= amount
# CALCULATE change = payment - amount
change = payment - amount

# IS change > 0?
if change > 0:
    d,q,i,n=0,0,0,0
    d = getDollars(change)
    change=change - d
    if change > 0:
        change_bkp = change
        q = getQuarters(round(change, 2))
        change=change - q*(0.25)
        i = getDimes(round(change, 2))
        change=change - i*(0.10)
        n = getNickels(round(change, 2))
        change = change - n*(0.05)

        #n=n+round(change_bkp* 2, 1)*10
        print("You got {} dollars, {} quarters, {} dimes, and {} nickels back in change" .format(d, q, i, n))
    else:
        print("You got {} dollars, {} quarters, {} dimes, and {} nickels back in change" .format(d, q, i, n))
else:
    print("No change owed")
