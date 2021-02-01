# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 07:09:51 2021

@author: lando

Day 11 AoC 2019
"""

import numpy as np
from IntCode import IntCode

instructions = list(map(int,open('input.txt','r').read().strip().split(',')))

def run_robot(hull,instructions):
    robot_coor = np.array([0,0])
    dirs = np.array([[-1,0],
                     [0,-1],
                     [1,0],
                     [0,1]])
    robot_dir = 0
    outputs = []
    
    def inp():
        if hull.get(tuple(robot_coor)) is None:
            return 0
        else:
            return hull.get(tuple(robot_coor))
    
    def out(x):
        outputs.append(x)
        return True
    
    robot = IntCode(instructions,inp,out)
    robot.run()
    while len(outputs) != 0:
        if len(outputs) == 2:
            color = outputs.pop(0)
            turn_right = outputs.pop(0)
            hull.update({tuple(robot_coor):color})
            if turn_right: robot_dir = (robot_dir - 1) % 4
            else: robot_dir = (robot_dir + 1) % 4
            robot_coor = robot_coor + dirs[robot_dir]
        robot.resume()
    return hull

# Part 1

hull = run_robot({},instructions)
ans = len(hull)
print(ans)

# Part 2
hull = run_robot({(0,0):1},instructions)
coors = np.array(tuple(hull.keys()))
arr = np.zeros((coors[:,0].max()-coors[:,0].min()+1,coors[:,1].max()-coors[:,1].min()+1))
coors = coors - coors.min(axis=0)
for key in hull:
    arr[key[0],key[1]] = hull[key]
print(arr[:,:arr.shape[1]//2])
print(arr[:,arr.shape[1]//2:])
# FARBCFJK