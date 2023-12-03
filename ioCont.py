# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:13:41 2023

@author: hokie
"""

def AoC_ReadIn(year=23,day=1,isSample=False):
    ext = "_sample.txt" if isSample else "_input.txt"
    
    file = open("C:\\Users\\hokie\\Programming\\AOC\\AOC" +
                str(year) + "\\Day" + str(day) + ext,'r')
    lines = file.readlines()
    return(lines)