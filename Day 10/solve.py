# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 10:31:46 2021

@author: lando

Aoc 2019 Day 10
"""

import math
import numpy as np

def find_asteroids(field):
    coors = np.where(field == '#')
    return np.vstack([coors[1],coors[0]]).T

def perspective(asteroids,ast):
    in_sight = {}
    for target in asteroids:
        if np.array_equal(ast,target):
            continue
        dist = target-ast
        a = math.gcd(dist[0],dist[1])
        angle = tuple(dist / math.gcd(dist[0],dist[1]))
        if in_sight.get(angle):
            in_sight[angle].append(a)
        else:
            in_sight.update({angle:[a]})
    return in_sight

def max_in_sight(asteroids):
    count = []
    for ast in asteroids:
        in_sight = perspective(asteroids,ast)
        count.append(len(in_sight))
        
    count = np.array(count)
    coor = asteroids[count == count.max()][0]
        
    return coor, count.max()

# example = ".#..#.....#####....#...##"
# ex_field = np.array(list(example))
# ex_field = ex_field.reshape((5,5))
asteroid_field = np.array([list(line.strip()) for line in open('input.txt','r').readlines()])
asteroids = find_asteroids(asteroid_field)
coor, ans = max_in_sight(asteroids)
print(ans)

# Part 2
        
def get_angles(directions):
    first = True
    for x, y in directions:
        try:
            angle = 90-math.degrees(math.atan(-y/x))
        except ZeroDivisionError:
            angle = 0
        if x < 0: angle += 180
        if first:
            angles = np.array([angle])
            first = False
        else:
            angles = np.hstack([angles,angle])
    return angles
            
def blast_asteroids(angles,in_sight,n):
    keys = list(in_sight.keys())
    while n > 0:
        for ind in np.argsort(angles):
            if n == 1:
                direction = keys[ind]
                mult = in_sight[direction][0]
                return np.array(direction), mult
            li = in_sight[keys[ind]]
            if li:
                li.remove(min(li))
                n -= 1

in_sight = perspective(asteroids,coor)
angles = get_angles(list(in_sight.keys()))
direction, mult = blast_asteroids(angles,in_sight,200)
bet = coor + direction * mult
ans = bet[0]*100 + bet[1]
print(ans)