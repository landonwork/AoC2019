# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:56:50 2021

@author: lando

AoC 2019 Day 8 Part 1
"""

import numpy as np
inp = open('input.txt','r').read().strip()
arr = np.array(list(inp)).astype(int)
arr = arr.reshape((len(inp)//150,6,25))

# Part 1
count = np.zeros((arr.shape[0],3))
for layer in range(arr.shape[0]):
    for n in range(3):
        count[layer,n] = (arr[layer] == n).sum()
        
layer_counts = count[count[:,0]==count[:,0].min()]
ans = layer_counts[:,1].sum() * layer_counts[:,2].sum()
print(ans)

# Part 2
image = arr[0]
for layer in range(arr.shape[0]):
    image[image==2] = arr[layer][image==2]
print(image) #CJZLP