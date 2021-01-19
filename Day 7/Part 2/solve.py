# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 01:03:26 2021

@author: lando

AoC 2019 Day 7 Part 2

This required adding a pause and resume functionality to the IntCode
class. For now, it can only be initiated through the output function.
Because of the resume function, I added the inp and out functions
as arguments in the constructor function so I won't have to keep 
passing them.
"""
from itertools import permutations
from IntCode import IntCode

instructions = [int(x) for x in open('input.txt','r').read().strip().split(',')]

relays = [[],[],[],[],[]]
thrusters = []
inp_fns = []
out_fns = []
for i in range(5):
    def inp():
        return relays[i%5].pop(0)
    def out(x):
        relays[(i+1)%5].append(x)
        return True
    inp_fns.append(inp)
    out_fns.append(out)
    
a = [IntCode(instructions,inp_fns[i],out_fns[i]) for i in range(5)]

for perm in permutations([5,6,7,8,9]):
    for i, n in enumerate(perm): relays[i].append(n)
    relays[0].append(0)
    
    i = 0
    while bool(relays[i%5]):
        if i < 5:
            a[i].run()
        else:
            a[i%5].resume()
        i+=1
    
    thrusters.append(relays[0].pop())
ans = max(thrusters)
print(ans)