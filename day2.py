# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 23:40:05 2023

@author: hokie
"""

class Game:

    def __init__(self,num):
        self.num = num
        self.pulls = list()
        
    def addPull(self,pull):
        self.pulls.append(pull)
        
    def getMaxes(self):
        maxBalls = dict(red=0,blue=0,green=0)
        for p in self.pulls:
            maxBalls["red"] = p.red if p.red > maxBalls["red"] else maxBalls["red"]
            maxBalls["blue"] = p.blue if p.blue > maxBalls["blue"]  else maxBalls["blue"]
            maxBalls["green"] = p.green if p.green > maxBalls["green"] else maxBalls["green"]
            
        return(maxBalls)
    
    def getPower(self):
        m = self.getMaxes()
        return(m["red"]*m["blue"]*m["green"])
    
class Pull:
    red = 0
    blue = 0
    green = 0
    
    # Assumes text is a single pull, un-parsed (i.e., comma-delimited)
    def __init__(self,txt):
        
        x = txt.split(sep=",")
        
        for i in range(len(x)):
            z = x[i].strip().split(" ")
            
            if z[1].find("red") >= 0:
                self.red = int(z[0])
            elif z[1].find("blue") >= 0:
                self.blue = int(z[0])
            elif z[1].find("green") >= 0:
                self.green = int(z[0])
                
    def __repr__(self):
        return("Red: "+ str(self.red) + "\tBlue: " + str(self.blue) + 
               "\tGreen: " + str(self.green))
        

def AoC_ReadIn(year=23,day=1,isSample=True):
    ext = "_sample.txt" if isSample else "_input.txt"
    
    file = open("C:\\Users\\hokie\\Programming\\AOC\\AOC" +
                str(year) + "\\Day" + str(day) + ext,'r')
    lines = file.readlines()
    return(lines)

txt = AoC_ReadIn(year=23,day=2,isSample=False)
games = list()

for x in txt:
    lns = x.split(sep=":")  # Separate the Game # from the outcomes
    
    gm = Game(lns[0].split(sep=" ")[1])
    
    outs = lns[1].split(sep=";")
    for p in outs:
        gm.addPull(Pull(p))
        
    games.append(gm)
    
val = 0
pwr = 0
for g in games:
    mx = g.getMaxes()
    if mx["red"] <= 12 and mx["green"] <= 13 and mx["blue"] <= 14:
        val += int(g.num)
    pwr += g.getPower()
        
print(val,pwr)