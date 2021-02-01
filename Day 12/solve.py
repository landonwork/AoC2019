# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 08:04:47 2021

@author: lando

AoC 2019 Day 12
"""

import re
import numpy as np
import math
from functools import reduce

def initialize():
    lines = [line.strip() for line in open('input.txt','r').readlines()]
    get_num = re.compile('=(?P<num>-?\d+)[,>]')
    p = np.zeros((len(lines),3),dtype=int)
    v = np.zeros(p.shape,dtype=int)
    
    for j, line in enumerate(lines):
        coors = []
        for i in range(3):
            if i == 0:
                match = get_num.search(line)
            else:
                match = get_num.search(line,match.span()[1])
            coors.append(int(match.group('num')))
        p[j] = np.array(coors,dtype=int)
    
    return p, v

# Part 1
def step(p,v):
    stack = np.stack((p,p,p,p)).swapaxes(0,1)
    greater = (p > stack).sum(axis=0)
    less    = (p < stack).sum(axis=0)
    v[:,:] = v + less - greater
    p[:,:] = p + v

def run_simulation(p,v,n):
    for i in range(n):
        step(p,v)
        
def total_energy(p,v):
    potential = np.abs(p).sum(axis=1)
    kinetic   = np.abs(v).sum(axis=1)
    return (potential * kinetic).sum()

p,v = initialize()
run_simulation(p,v,1000)
ans = total_energy(p,v)
print(ans)

# Part 2

def find_periods(p,v):
    i = 1
    start = p.copy()
    periods = [0] * p.shape[0]
    step(p,v)
    while 0 in periods:
        if i % 1000000 == 0:
            print(i)
        for j in range(p.shape[0]):
            if np.array_equal(p[j],start[j]) and bool(periods[j]):
                periods[j] = i
                print(periods)
        step(p,v)
        i += 1
    return periods
    
p, v = initialize()
periods = find_periods(p,v)

ans = reduce(lambda x,y:x*y/math.gcd(int(x),int(y)),periods)
# Didn't work :/