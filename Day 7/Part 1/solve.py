# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:37:46 2021

@author: lando

AoC 2019 Day 7
"""
from IntCode import IntCode
from itertools import permutations

instructions = [int(x) for x in open('input.txt','r').read().strip().split(',')]
a = IntCode(instructions)

# Part 1
relay = []
thrusters = []
def out(x):
    relay.append(x)
for perm in permutations([0,1,2,3,4]):
    signal = 0
    for setting in perm:
        relay.append(signal)
        relay.append(setting)
        a.run(lambda : relay.pop(), lambda x:relay.append(x))
        signal = relay.pop()
    thrusters.append(signal)
ans = max(thrusters)
print(ans)