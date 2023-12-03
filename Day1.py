# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:13:18 2023

@author: hokie
"""

#from ioCont.py import AoC_ReadIn
from re import findall

numstrs = {"one":"1",
       "two":"2",
       "three":"3",
       "four":"4",
       "five":"5",
       "six":"6",
       "seven":"7",
       "eight":"8",
       "nine":"9"}

replacements = {
"zerone": "zeroone",
"oneight": "oneeight",
"twone": "twoone",
"sevenine": "sevennine",
"eightwo": "eighttwo",
"eighthree": "eightthree",
"nineight": "nineeight"
}

def AoC_ReadIn(year=23,day=1,isSample=False):
    ext = "_sample.txt" if isSample else "_input.txt"
    
    file = open("C:\\Users\\hokie\\Programming\\AOC\\AOC" +
                str(year) + "\\Day" + str(day) + ext,'r')
    lines = file.readlines()
    return(lines)

def replace(mytx):
    for x in replacements.keys():
        mytx = mytx.replace(x,replacements[x])
    
    return(mytx)

def fix(mytx):    
    dex = 1000
    nStr = ""
    for num in numstrs.keys():
        if mytx.find(num) > -1 and mytx.find(num) < dex:
            nStr = num
            dex = mytx.find(num)
        if dex == 0:
            break
    
    if dex == 1000:
        return(mytx)
    else:
        mytx = mytx.replace(nStr,numstrs[nStr])
        return(fix(mytx))

txt = AoC_ReadIn(year=23,day=1,isSample=False)
val = [0,0]

for x in txt:
    z = replace(x)
    y = fix(z)
    
    for i in range(2):
        digs = findall("\d",x) if i==0 else findall("\d",y)
        if len(digs) > 0:
            val[i] += int(digs[0] + digs[len(digs)-1])
            
            if i == 1:
                print(int(digs[0] + digs[len(digs)-1]))
               
        
print(val)
    
