# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:29:08 2021

@author: lando

AoC 2019
Day 14
"""

def get_recipes(recipes:list):
    ingredient_list = []
    result_list = []
    amounts = []
    for recipe in recipes:
        
        recipe = recipe.split('=>')
        # print(recipe)
        ingredients = recipe[0].strip().split(', ')
        result = recipe[1].strip()
        
        for i in range(len(ingredients)):
            ingredients[i] = ingredients[i].split(' ')
        result = result.split(' ')

        result_list.append(result[1])
        ingredient_list.append(tuple([ing[1] for ing in ingredients]))
        amounts.append(tuple([int(ing[0]) for ing in ingredients] + [int(result[0])]))
        
    return ingredient_list, result_list, amounts

def fuel_cost(ings,results,amts):
    ore_costs = {'ORE':1}
    while 'FUEL' not in ore_costs.keys():
        i = 0
        while i < len(results):
            if all([ing in ore_costs.keys() for ing in ings[i]]):
                amt = sum(map(lambda j : amts[i][j]*ore_costs[ings[i][j]],range(len(ings[i])))) / amts[i][-1]
                ore_costs.update({results[i]:amt})
                ings.pop(i); results.pop(i); amts.pop(i)
                continue
            i += 1
        print(len(ore_costs))
        if len(ore_costs) > 59:
            print(ore_costs)
    return ore_costs['FUEL']

lines = open('input.txt','r').readlines()
ingredients, results, amounts = get_recipes(lines)
print(fuel_cost(ingredients, results, amounts))