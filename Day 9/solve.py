# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:13:11 2021

@author: lando

AoC 2019 Day 9
"""

from IntCode import IntCode
instructions = [int(x) for x in open('input.txt.','r').read().strip().split(',')]
a = IntCode(instructions,input,print)
a.run()

# Parts 1 and 2 take keyboard input