# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 12:44:56 2021

@author: lando

AoC 2019 Day 2
"""
import numpy as np
line = open('input.txt','r').read().strip().split(',')
arr = np.array(line).astype(int)
noun = 12; verb = 2
arr[1] = noun; arr[2] = verb

def int_code(arr):
    i = 0
    val = 0
    def add(i): arr[arr[i+3]] = arr[arr[i+1]] + arr[arr[i+2]]
    def mult(i): arr[arr[i+3]] = arr[arr[i+1]] * arr[arr[i+2]]
    ops = {1:add,2:mult,99:lambda x:True}
    while val != 99:
        val = arr[i]
        # print(i,val)
        assert val in ops.keys(), 'Invalid operator'
        if bool(ops[val](i)):
            break
        else:
            i += 4
    return arr

# Part 1
arr = int_code(arr)
print(arr[0])

# Part 2
def initialize(noun,verb):
    line = open('input.txt','r').read().strip().split(',')
    arr = np.array(line).astype(int)
    arr[1] = noun; arr[2] = verb
    return arr

def find_value(target):
    ans = 0
    noun = 0; verb = 0
    while True:
        while True:
            arr = initialize(noun,verb)
            arr = int_code(arr)
            ans = arr[0]
            if ans == target:
                return 100*noun+verb
            elif ans > target or verb > 99:
                verb = 0
                break
            else:
                verb += 1
        noun += 1
            