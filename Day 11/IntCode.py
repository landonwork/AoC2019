# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 14:41:05 2021

@author: lando

IntCode class developed for AoC 2019
"""
import numpy as np


class IntCode:
    
    def __init__(self, code, fn1, fn2):
        
        def inp():
            self.run_code[self.get_address(1)] = int(fn1())
            self.pos += 2
        
        def out():
            self.pause = fn2(self.get_params(1)[0])
            self.pos += 2
            
        self.ops = [None, self.add, self.mult, inp, out, self.jumpif,
                    self.jumpifnot, self.lessthan, self.equalto,
                    self.move_base]
        self.modes = [self.param,self.immediate,self.relative]
        self.code = np.hstack([np.array(code).astype(float),np.zeros((1000,),dtype=float)])
        self.pause = False
        
    def run(self):
        
        self.run_code = self.code.copy()
        self.pos = 0
        self.base = 0
        self.resume()
        
    def resume(self):
        while self.run_code[self.pos] != 99:
            opcode = int(self.run_code[self.pos])
            self.ops[opcode % 100]()
            if self.pause:
                self.pause = False
                break    
    
    def add(self):
        addends = self.get_params(2)
        self.run_code[self.get_address(3)] = np.add(addends[0],addends[1])
        self.pos += 4
            
    def mult(self):
        factors = self.get_params(2)
        self.run_code[self.get_address(3)] = np.multiply(factors[0],factors[1])
        self.pos += 4
        
    def jumpif(self):
        a, b = self.get_params(2)
        if a != 0: self.pos = int(b)
        else: self.pos += 3
    
    def jumpifnot(self):
        a, b = self.get_params(2)
        if a == 0: self.pos = int(b)
        else: self.pos += 3
    
    def lessthan(self):
        a, b = self.get_params(2)
        self.run_code[self.get_address(3)] = int(a < b)
        self.pos += 4
    
    def equalto(self):
        a, b = self.get_params(2)
        self.run_code[self.get_address(3)] = int(a == b)
        self.pos += 4
        
    def move_base(self):
        a, = self.get_params(1)
        self.base += int(a)
        self.pos += 2
    
    def get_params(self,n):
        params = []
        for i in range(1,n+1):
            mode_n = int(self.run_code[self.pos])//(10**(i+1)) % 10
            params.append(self.modes[mode_n](self.pos+i))
        return tuple(params)
    
    def get_address(self,n):
        mode_n = int(self.run_code[self.pos])//(10**(n+1))
        if mode_n:
            return int(self.base+self.run_code[self.pos+n])
        else:
            return int(self.run_code[self.pos+n])
    
    def param(self,p):
        return self.run_code[int(self.run_code[p])]
    
    def immediate(self,p):
        return self.run_code[p]
    
    def relative(self,p):
        return self.run_code[self.base+int(self.run_code[p])]