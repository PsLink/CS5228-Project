import fileinput
import random

maximum = 0
ID = 0
for i in fileinput.input("tree0.txt"):
  table = i.split()

  # check if the table is missed or anything
  #if random.random()>0.95:
  #  print table[0],len(table)-1
  if maximum < len(table)-1:
    maximum = len(table)-1
    ID = table[0]
print ID,maximum


