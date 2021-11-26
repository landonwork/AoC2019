# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 10:29:08 2021

@author: lando

AoC 2019
Day 14
"""
from typing import List, Dict, Optional
import pandas as pd

def get_recipes(recipes: List[str]):
    chems = {}
    for recipe in recipes:
        
        recipe = recipe.split('=>')
        ingredients = recipe[0].strip().split(', ')
        chem = recipe[1].strip().split(' ')
        qty = int(chem[0])
        name = chem[1]
        inp = {ing.split(' ')[1]: int(ing.split(' ')[0]) for ing in ingredients}
        chems.update({name: {'in': inp, 'out': qty}})
    
    return chems

def fuel_cost(chems: dict, n: int):
    
    df = pd.DataFrame({
        'chem': ['ORE'] + list(chems.keys()),
        'total': 0,
        'in_use': 0,
    }).set_index('chem')
    df.loc['FUEL','in_use'] = n
    
    def reconcile(chem: str):
        # Recursion, baby first; Depth first mutation
        if chem == 'ORE':
            df.loc['ORE','total'] = df.loc['ORE','in_use']
        # First we find out how many MORE recipes we need to make in order to
        # meet the required amount
        total = df.loc[chem,'total']
        req = df.loc[chem,'in_use']
        more = req - total
        if more <= 0: # If total current is greater than the required quantity,
            return None # do nothing
        more_factor = (more - 1) // chems[chem]['out'] + 1
        df.loc[chem,'total'] += more_factor * chems[chem]['out']
        assert df.loc[chem,'total'] >= df.loc[chem,'in_use']
        for ing in chems[chem]['in'].keys():
            df.loc[ing,'in_use'] += more_factor * chems[chem]['in'][ing]
            reconcile(ing)
        # Then we need to change the total value of chem (as well as left_over)
        # Then we need to change the in use values of each input and 
        # reconcile those one at a time
        # And when we get to ORE, we just set total equal to in use and return
        
    reconcile('FUEL')
    return df.loc['ORE','total']

def binary_search(chems: dict, n: int):
    lo = 1
    hi = None
    guess = 1
    while True:
        g = fuel_cost(chems, guess) > n
        if g: # If we surpassed our limit,
            hi = guess
        else:
            lo = guess
        if hi is None:
            guess = lo * 2
        else:
            guess = (lo + hi) // 2
        if guess == lo or guess == hi:
            break
    return lo
            
if __name__ == '__main__':
    lines = open('input.txt','r').readlines()
    recipes = get_recipes(lines)
    print(fuel_cost(recipes, 1))
    print(binary_search(recipes, 1e12))