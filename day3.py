# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:27:27 2023

@author: hokie
"""

import re
from ioCont import AoC_ReadIn

txt = AoC_ReadIn(year=23,day=3,isSample=False)

def check(row,low,hi):
    ln = txt[row]
    sub = ln[low:hi]
    return False if re.search(r'[-!@#$%^&*()_+?/<>=]+',sub) == None else True

def checkGear(row,low,hi,mults):
    ln = txt[row]
    nums = re.finditer("\d+",ln)
    for n in nums:
        if len(set(
                range(n.start(),n.end())).intersection(set(range(
                    low,hi)))) > 0: 
            mults.append(ln[n.start():n.end()])
    
dex = 0
val = 0
for t in txt:
    matches = re.finditer(r'\d+',t)
    for m in matches:
        s = m.start()
        e = m.end()
    
        if (s > 0 and check(dex,s-1,s)) or \
            (e < len(t) and check(dex,e,e+1)) or \
            (dex > 0 and check(dex-1,max([0,s-1]),min([len(t),e+1]))) or \
            (dex < len(txt)-1 and check(dex+1,max([0,s-1]),min([len(t),e+1]))):
                val += int(t[s:e])
    dex += 1
    
print("Part 1: " + str(val))

dex = 0
val = 0
for t in txt:
    t = t.strip()
    matches = re.finditer(r'\*+',t)
    for m in matches:
        s = m.start()
        e = m.end()
    
        mults = list()
        if (s > 0):
            checkGear(dex,s-1,s,mults)
        if (e < len(t)):
            checkGear(dex,e,e+1,mults)
        if (dex > 0):
            checkGear(dex-1,max([0,s-1]),min([len(t),e+1]),mults)
        if (dex < len(txt)-1):
            checkGear(dex+1,max([0,s-1]),min([len(t),e+1]),mults)
                
        if len(mults) == 2:
            val += int(mults[0])*int(mults[1])
    dex += 1
    
print("Part 2: " + str(val))
    

