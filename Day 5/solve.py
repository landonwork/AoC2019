# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 12:06:04 2021

@author: lando

AoC 2019 Day 5
"""

import numpy as np

# Parts 1 and 2
class IntCode:
    
    def __init__(self,code):
        self.code = code
        
    def run(self,fn1,fn2):
        
        def inp():
            self.run_code[self.run_code[self.pos+1]] = int(fn1())
            self.pos += 2
        
        def out():
            fn2(self.run_code[self.run_code[self.pos+1]])
            self.pos += 2
    
        self.ops = [None,self.add,self.mult,inp,out,
                    self.jumpif,self.jumpifnot,self.lessthan,self.equalto]
        self.modes = [self.param,self.immediate]
        self.run_code = self.code.copy()
        self.pos = 0
        
        while self.run_code[self.pos] != 99:
            opcode = self.run_code[self.pos]
            self.ops[opcode%100]()
    
    def add(self):
        addends = self.get_params(2)
        self.run_code[self.run_code[self.pos+3]] = np.add(addends[0],addends[1])
        self.pos += 4
            
    def mult(self):
        factors = self.get_params(2)
        self.run_code[self.run_code[self.pos+3]] = np.multiply(factors[0],factors[1])
        self.pos += 4
        
    def jumpif(self):
        a, b = self.get_params(2)
        if a != 0: self.pos = b
        else: self.pos += 3
    
    def jumpifnot(self):
        a, b = self.get_params(2)
        if a == 0: self.pos = b
        else: self.pos += 3
    
    def lessthan(self):
        a, b = self.get_params(2)
        self.run_code[self.run_code[self.pos+3]] = int(a < b)
        self.pos += 4
    
    def equalto(self):
        a, b = self.get_params(2)
        self.run_code[self.run_code[self.pos+3]] = int(a == b)
        self.pos += 4
    
    def get_params(self,n):
        params = []
        for i in range(1,n+1):
            mode_n = self.run_code[self.pos]//(10**(i+1)) % 10
            params.append(self.modes[mode_n](self.pos+i))
        return tuple(params)
    
    def param(self,p):
        return self.run_code[self.run_code[p]]
    
    def immediate(self,p):
        return self.run_code[p]
    
instructions = [int(x) for x in open('input.txt','r').read().strip().split(',')]
a = IntCode(instructions)
a.run(input,print)