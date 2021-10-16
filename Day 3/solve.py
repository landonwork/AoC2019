# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 22:37:18 2021

@author: lando
"""

import numpy as np

def map_wire(li):
    coor = [0,0]
    wire = []
    for segment in li:
        axis = int(segment[0] in ('U','D'))
        dist = (-1 if segment[0] in ('D','L') else 1) * int(segment[1:])
        wire.append({'coor':tuple(coor),'axis':axis,'dist':dist})
        coor[axis] += dist
    return wire

def is_intersection(seg1,seg2):
    coor = [0,0]
    if seg1['axis'] == seg2['axis']:
        return None
    else:
        axis1 = seg1['axis']
        before1 = np.sign(seg1['coor'][axis1]-seg2['coor'][axis1])
        after1 = np.sign(seg1['coor'][axis1]+seg1['dist']-seg2['coor'][axis1])
        if before1 == after1:
            return None
        axis2 = seg2['axis']
        before2 = np.sign(seg2['coor'][axis2]-seg1['coor'][axis2])
        after2 = np.sign(seg2['coor'][axis2]+seg2['dist']-seg1['coor'][axis2])
        if before2 == after2:
            return None
        coor[axis2] = seg1['coor'][axis2]
        coor[axis1] = seg2['coor'][axis1]
        return tuple(coor)

# Part 1
lines = [line.strip().split(',') for line in open('C:/Users/lando/Desktop/Python/Advent of Code 2019/Day 3/input.txt','r').readlines()]
wires = [map_wire(line) for line in lines]
intersections = []
for seg1 in wires[0]:
    for seg2 in wires[1]:
        x = is_intersection(seg1,seg2)
        if x is not None: intersections.append(x)
        
ans = 9999999999
for x in intersections:
    ans = min(ans,abs(x[0])+abs(x[1]))
print(ans)

# Part 2
def delay(wire, coor):
    dist = 0
    for seg in wire:
        axis = seg['axis']
        if seg['coor'][1-axis] != coor[1-axis]:
            dist += abs(seg['dist'])
        elif np.sign(seg['coor'][axis]-coor[axis]) != np.sign(seg['coor'][axis]+seg['dist']-coor[axis]):
            dist += abs(seg['coor'][axis]-coor[axis])
            return dist
        else:
            dist += abs(seg['dist'])

ans = 999999999
for x in intersections:
    print(x)
    ans = min(ans,delay(wires[0],x)+delay(wires[1],x))
print(ans)