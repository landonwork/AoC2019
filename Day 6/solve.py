# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:22:03 2021

@author: lando

AoC 2019 Day 6
"""

satellites = {}
for line in open('input.txt','r').readlines():
    satellites.update({line.strip()[-3:]:line[:3]})

# Part 1
def count_orbits(d):
    n = 0
    for sat in d.keys():
        while sat != 'COM':
            sat = d[sat]
            n += 1
    return n

print(count_orbits(satellites))

# Part 2
SAN_path = ['SAN']
while SAN_path[-1] != 'COM':
    SAN_path.append(satellites[SAN_path[-1]])

YOU_path = ['YOU']
while YOU_path[-1] not in SAN_path:
    YOU_path.append(satellites[YOU_path[-1]])

ans = len(YOU_path) + SAN_path.index(YOU_path[-1]) - 3
print(ans)