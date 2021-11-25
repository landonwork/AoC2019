# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:59:57 2021

@author: lando

Advent of Code 2019
Day 13
"""

from IntCode import IntCode

instructions = open('input.txt').read().strip()

# Part 1

li = []

def out(x):
    li.append(x)
    
a = IntCode(instructions.split(','),input,out)

a.run()
tiles = {}
for i in range(0,len(li),3):
    tiles[tuple(li[i:i+2])] = li[int(i+2)]
    
ans = 0
for x in tiles.values(): ans += x == 2
print(ans)

# Part 2

instructions = open('input.txt').read().strip()
instructions = [int(i) for i in instructions.split(',')]
instructions[0] = 2

display = [0]
grid = {}
coors = [0,0]
n = [1]
def out2(x):
    if n[0] % 3:
        coors[n[0]%3-1] = x
    else:
        if tuple(coors) == (-1.,0.):
            display[0] = x
        else:
            grid[tuple(coors)] = x
    n[0] += 1
            
def inp2():
    ball, paddle = None, None
    for coors, val in grid.items():
        if val == 4.:
            ball = coors
        if val == 3.:
            paddle = coors
    if paddle[0] > ball[0]:
        return -1
    if paddle[0] < ball[0]:
        return 1
    return 0

a = IntCode(instructions,inp2,out2)

a.run()
print(display[0])