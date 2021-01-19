# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:20:15 2021

@author: lando

AoC 2019 Day 1
"""

def fuel(mass):
    return max(mass//3 - 2,0)

# Part 1
ans = sum([fuel(int(text.strip())) for text in open('input.txt','r').readlines()])
print(ans)

# Part 2
def fuel_requirement(mass):
    req = 0
    while mass != 0:
        mass = fuel(mass)
        req += mass
    return req

ans = sum([fuel_requirement(int(text.strip())) for text in open('input.txt','r').readlines()])
print(ans)
