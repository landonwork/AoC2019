# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 14:06:06 2021

@author: lando
"""
import numpy as np
from IntCode import IntCode
from typing import Tuple, List
from functools import reduce
from copy import copy


# Movement commands:
# north (1), south (2), west (3), and east (4)
# Status codes:
# 0: The repair droid hit a wall. Its position has not changed.
# 1: The repair droid has moved one step in the requested direction.
# 2: The repair droid has moved one step in the requested direction; its new position is the location of the oxygen system.

class Node:
    """"""
    def __init__(self, name: Tuple[int, int], g: 'LatticeGraph'):
        
        self.name = name # (row, col)
        
        self.north_node = g.nodes.get(self.north, None)
        if self.north_node is not None:
            self.north_node.south_node = self
            
        self.south_node = g.nodes.get(self.south, None)
        if self.south_node is not None:
            self.south_node.north_node = self
            
        self.west_node = g.nodes.get(self.west, None)
        if self.west_node is not None:
            self.west_node.east_node = self
            
        self.east_node = g.nodes.get(self.east, None)
        if self.east_node is not None:
            self.east_node.west_node = self
            
        g.add_node(self)
    
    @property
    def north(self):
        return (self.name[0]-1, self.name[1])
    @property
    def south(self): # We're going to make things a little easier ono ourselves
        return (self.name[0]+1, self.name[1])
    @property
    def west(self): # We're going to make things a little easier ono ourselves
        return (self.name[0], self.name[1]-1)
    @property
    def east(self):
        return (self.name[0], self.name[1]+1)
    
class Wall(Node):
    def __init__(self, name: Tuple[int, int], g: 'LatticeGraph'):
        return super().__init__(name,g)

class O2(Node):
    def __init(self, name: Tuple[int, int], g: 'LatticeGraph'):
        return super().__init__(name,g)

class LatticeGraph:
    """"""
    def __init__(self):
        self.nodes={}
    
    def add_node(self, n: 'Node'):
        self.nodes[n.name] = n
        
command = [1]
status = [1]

inp = lambda : command[0]
def out(x):
    status[0] = int(x)
    return True


def explore() -> 'LatticeGraph':
    s = open('input.txt','r').read().strip()
    droid = IntCode(s.split(','), inp, out)
    g = LatticeGraph()
    current = Node((0,0),g)
    recurse(current, None, droid, g)
    return g

def recurse(current: 'Node', back: int, droid: 'IntCode', g: 'LatticeGraph') -> None:
    directions = [None,'north','south','east','west']
    for d in range(1,5):
        if getattr(current,directions[d]+'_node') is None:
            command[0] = d
            if getattr(droid, 'pos', None) is None:
                droid.run()
            else:
                droid.resume()
        else:
            continue
        if status[0] == 0:
            Wall(getattr(current, directions[d]), g)
        elif status[0] == 1:
            n = Node(getattr(current, directions[d]), g)
            come_back = d - 1 + 2 * (d % 2)
            recurse(n, come_back, droid, g)
        elif status[0] == 2:
            n = O2(getattr(current, directions[d]), g)
            come_back = d - 1 + 2 * (d % 2)
            recurse(n, come_back, droid, g)
        else:
            raise ValueError(f"Unknown status: {status[0]}")
    if back is not None:
        command[0] = back
        droid.resume()
    
g = explore()
print(g.nodes)

def print_map(g):
    min_row, max_row = 0, 0
    min_col, max_col = 0, 0
    for t in g.nodes.keys():
        min_row = min(min_row, t[0])
        max_row = max(max_row, t[0])
        min_col = min(min_col, t[1])
        max_col = max(max_col, t[1])
    
    the_map = np.full((max_row-min_row+1, max_col-min_col+1), '.')
    for t, n in g.nodes.items():
        if isinstance(n, Wall):
            the_map[t[0]-min_row,t[1]-min_col] = '#'
        elif isinstance(n, O2):
            the_map[t[0]-min_row,t[1]-min_col] = 'O'
    the_map[min_row,min_col] = 'D'
    # for row in range(the_map.shape[0]):
    #     print(*the_map[row,:],sep='')
    return '\n'.join([''.join(the_map[i,:]) for i in range(the_map.shape[0])])

the_map = print_map(g)

def shortest_path(g: 'LatticeGraph'):
    current = g.nodes[(0,0)]
    path = []
    path = recurse2(current, path, None)
    return path

def recurse2(current: Node, path: List[int], min_path: List[int]):
    directions = ['north','south','east','west']
    if isinstance(current, O2):
        if min_path is None or len(path) < len(min_path):
            min_path = copy(path)
        return min_path
    for d in directions:
        if len(path) > 0 and path[-1] == opposite(d):
            continue
        look_ahead = getattr(current,d+'_node')
        if isinstance(look_ahead, Wall):
            continue
        else:
            new_path = recurse2(look_ahead, path+[d], min_path)
            if new_path is not None:
                if min_path is None:
                    min_path = copy(new_path)
                else:
                    if len(new_path) < (len(min_path)):
                        min_path = copy(new_path)
    return min_path

def opposite(d: str):
    opps = {
        'north': 'south',
        'south': 'north',
        'west': 'east',
        'east': 'west'
    }
    return opps[d]

path = shortest_path(g)
print(len(path))

def fill_with_O2(g: 'LatticeGraph'):
    directions = ['north','south','east','west']
    new_O2 = {n.name for n in g.nodes.values() if isinstance(n,O2)}
    count = 0
    while len(new_O2) != 0:
        li = copy(new_O2)
        new_O2 = set()
        for name in li:
            current = g.nodes[name]
            for d in directions:
                look_ahead = getattr(current,d+'_node')
                if not isinstance(look_ahead, Wall) and not isinstance(look_ahead, O2):
                    O2(look_ahead.name, g)
                    new_O2.add(look_ahead.name)
        count += 1
    return count-1 # The last iteration just checks that there was no new O2

print(fill_with_O2(g))