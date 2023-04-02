#!/bin/python3

import random

def gra():
  
  print("Prosze wybrac liczbe od 1 do 20")
  
  inp = 0
  while (inp < 1 and inp > 20):
    inp = int(input())
    
   rl = random.randint(1,20)
  
  if (inp == rl):
    print("Win")
  else:
    print("Fail")
    
print("Game starts")

ch = "y"
while (ch == "y"):
  gra()
  print("Want to play 1 more?")
  ch = input()
