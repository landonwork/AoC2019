# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 10:35:01 2021

@author: lando

AoC 2019 Day 4
"""

import re

# My input
lo, hi = 234208, 765869

# Part 1
def criterion1(x):
    return re.search('(?P<b>\d)(?P=b)',str(x)) is not None

def criterion2(x):
    digits = [int(digit) for digit in str(x)]
    for i in range(len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    return True

ans = 0
for x in range(lo,hi+1):
    ans += criterion1(x) & criterion2(x)
print(ans)

# Part 2
def criterion3(x):
    for i in range(1,10):
        if str(x).count(str(i)) == 2:
            return True
    return False

ans = 0
for x in range(lo,hi+1):
    # if (criterion1(x) & criterion2(x)) and not (criterion2(x) & criterion3(x)):
    #     print(x)
    ans += criterion2(x) & criterion3(x)
print(ans)