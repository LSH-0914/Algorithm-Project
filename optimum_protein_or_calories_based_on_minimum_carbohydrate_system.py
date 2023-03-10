# -*- coding: utf-8 -*-
"""Optimum Protein or Calories  based on Minimum Carbohydrate System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G2smxRQAdfEbsGMPlGVVCD8qnVMqkweR
"""

import pandas as pd
import math
from collections import OrderedDict
df = pd.read_csv("//content//nutrients_csvfile.csv",encoding='latin1')
df

category = []
for i in range(0,len(df)):
  category.append(df["Category"][i])

test_list = list(OrderedDict.fromkeys(category))

print(len(test_list))

print("Category: ")

for i in test_list:
  print(i)
a = input("\nEnter your allergies: ")

food = []
carbs = []
protein = []
b = input("Do you want to choose Protein or Calories to be maximized? Please enter P for Protein or C for Calories:  ")
if(b == "P"):
  target = "Protein"
  for i in range(0,len(df)):
    if(df["Category"][i] != a):
      food.append(df["Food"][i])
      protein.append(math.ceil(df["Protein/100g"][i]))
      carbs.append(math.ceil(df["Carbs/100g"][i]))
else:
  target = "Calories"
  for i in range(0,len(df)):
    if(df["Category"][i] != a):
      food.append(df["Food"][i])
      protein.append(math.ceil(df["Calories/100g"][i]))
      carbs.append(math.ceil(df["Carbs/100g"][i]))

prioritize = []
prioritize1 = []
prioritize2 = []

for i in food:

  print(i)

a = "Y"
while(a == "Y"):
  c = input("What food items would you like to prioritize?\n")
  quantity = int(input("Quantity of this type of food item would you like to consume(*100g)?\n"))
  for i in range(0,len(food)):
    if food[i] == c:
      for j in range(0,quantity):
        prioritize.append(food[i])
        prioritize1.append(protein[i])
        prioritize2.append(carbs[i])
      
  a = input("Press Y to enter more food prioritization or N to finish: ")

for i in range(0,len(prioritize)):
  print(prioritize[i])
  print(prioritize1[i])
  print(prioritize2[i])

new_prioritize = list(set(prioritize))
print(new_prioritize)
for j in range(0, len(new_prioritize)):
  a =food.index(new_prioritize[j])
  food.remove(new_prioritize[j])
  protein.pop(a)
  carbs.pop(a)

print(new_prioritize)

print(prioritize)

print(prioritize2)

# carbs = prioritize2 + carbs
# protein = prioritize1 + protein
# food = prioritize + food

# A naive recursive implementation
# of 0-1 Knapsack Problem
 
# Returns the maximum value that
# can be put in a knapsack of
# capacity W
 

# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem
 
# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, name, wt, val, n,prioritize,prioritize1,prioritize2,sum,target):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    print("Optimum "+ target+"(g) obtained by Knapsack 0-1 algorithm: "+str(res + total1)+ "\n")
    print("The distribution of Carbohydrate and", target ,"as well as suggested food are displayed as below: \n")
    print("Carbohydrate(g)\t"+ target +"\tQuantity"+"\tFood")
    count = 0
    prioritize_item = prioritize[0]
    for i in range(0,len(prioritize)):
      if (prioritize_item == prioritize[i]):
        count+=1
        if(count == prioritize.count(prioritize[i])):
          print(str(prioritize2[i] * count)+"\t\t"+str(prioritize1[i] * count)+ "\t"+str(count)+"\t\t"+str(prioritize[i]))
          count = 0
      else:
        count+=1
        if(count == prioritize.count(prioritize[i])):
          print(str(prioritize2[i] * count)+"\t\t"+str(prioritize1[i] * count)+ "\t"+str(count)+"\t\t"+str(prioritize[i]))
          count = 0
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            print(str(wt[i - 1])+"\t\t"+str(val[i-1])+"\t"+str(1)+"\t\t"+name[i-1])
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
 

  
# Driver Code
total = 0
total1 = 0
for i in range(0,len(prioritize)):
  total += prioritize2[i]
  total1 += prioritize1[i]

W = int(input("How many Carbs (in grams) do you plan to consume? ")) - total
n = len(carbs)
printknapSack(W,food, carbs, protein, n,prioritize,prioritize1,prioritize2,total1,target)

def fractional_knapsack(value, weight, capacity,prioritize,prioritize1,prioritize2,food,total,target):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    print("\nThe distribution of Carbohydrate and", target ,"as well as suggested food are displayed as below: \n")
    print("Carbs\t"+target+"\tFraction\tItem")
    count = 0
    prioritize_item = prioritize[0]
    for i in range(0,len(prioritize)):
      if (prioritize_item == prioritize[i]):
        count+=1
        if(count == prioritize.count(prioritize[i])):
          print(str(prioritize2[i])+"\t"+str(prioritize1[i])+"\t"+str(count)+"\t\t"+prioritize[i])
          count = 0
      else:
        count+=1
        if(count == prioritize.count(prioritize[i])):
          print(str(prioritize2[i])+"\t"+str(prioritize1[i])+"\t"+str(count)+"\t\t"+prioritize[i])
          count = 0  
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
            print(str(weight[i])+"\t"+ str(value[i])+"\t"+str(fractions[i])+"\t\t"+food[i])
        else:
            fractions[i] = capacity/weight[i]
            factional_value = value[i]*capacity/weight[i]
            max_value += factional_value
            print(str(weight[i])+"\t"+ str(round(factional_value,2))+"\t"+str(round(fractions[i],2))+"\t\t"+food[i])
            break
 
    print('\nOptimum '+ target + "(g) obtained by fractional knapsack algorithm: " + str(round(float(max_value+total1),2)))
 
total = 0
total1 = 0 
for i in range(0,len(prioritize)):
  total += prioritize2[i]
  total1 += prioritize1[i]

item = food
value = protein
weight = carbs
capacity = int(input('How many Carbs (in grams) do you plan to consume? ')) - total
 
fractional_knapsack(value, weight, capacity,prioritize,prioritize1,prioritize2,food,total1,target)

print(len(protein))

print(len(carbs))

print(food)

print(carbs)

carbs = carbs[0:10]
protein = protein[0:10]
food = food[0:10]

# A naive recursive implementation
# of 0-1 Knapsack Problem
 
# Returns the maximum value that
# can be put in a knapsack of
# capacity W
 

# Python3 code for Dynamic Programming
# based solution for 0-1 Knapsack problem
 
# Prints the items which are put in a
# knapsack of capacity W
def printknapSack(W, name, wt, val, n,target):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    print("Optimum " + target +"(g) obtained by Knapsack 0-1 algorithm: " + str(res) + "\n")
    print("The distribution of Carbohydrate and Protein as well as suggested food are displayed as below: \n")
    print("Carbohydrate(g) "+ target + "(g) " +"Food")
     
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
 
            # This item is included.
            print(wt[i - 1],val[i-1],name[i-1])
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
 

  
# Driver Code
print("Test correctness of knapsack 0-1 algorithm using 10 food items \n")
W = int(input("How many Carbs (in grams) do you plan to consume? "))
n = len(carbs)
printknapSack(W,food, carbs, protein, n,target)

def fractional_knapsack(value, weight, capacity,food,target):
    """Return maximum value of items and their fractional amounts.
 
    (max_value, fractions) is returned where max_value is the maximum value of
    items with total weight not more than capacity.
    fractions is a list where fractions[i] is the fraction that should be taken
    of item i, where 0 <= i < total number of items.
 
    value[i] is the value of item i and weight[i] is the weight of item i
    for 0 <= i < n where n is the number of items.
 
    capacity is the maximum weight.
    """
    # index = [0, 1, 2, ..., n - 1] for n items
    index = list(range(len(value)))
    # contains ratios of values to weight
    ratio = [v/w for v, w in zip(value, weight)]
    # index is sorted according to value-to-weight ratio in decreasing order
    index.sort(key=lambda i: ratio[i], reverse=True)

    max_value = 0
    fractions = [0]*len(value)
    print("\nItems in Knapsack: ")
    print("Carbs\t" + target+"\tFraction\tItem")
  
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
            print(str(weight[i])+"\t"+ str(value[i])+"\t"+str(fractions[i])+"\t\t"+food[i])
        else:
            fractions[i] = capacity/weight[i]
            factional_value = value[i]*capacity/weight[i]
            max_value += factional_value
            print(str(weight[i])+"\t"+ str(factional_value)+"\t"+str(fractions[i])+"\t\t"+food[i])
            break
 
    print('Optimum Protein:', float(max_value+total1))
 


item = food[0:10]
value = protein[0:10]
weight = carbs[0:10]
capacity = int(input('How many Carbs (in grams) do you plan to consume? '))
fractional_knapsack(value, weight, capacity,food,target)