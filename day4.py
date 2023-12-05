# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 21:05:32 2023

@author: hokie
"""

from ioCont import AoC_ReadIn

class Card:
    def __init__(self,iStr):
        ln = iStr.split() # Separate by whitespace
        
        self.num = int(ln[1][0:len(ln[1])-1])
        
        self.winners = set()
        self.numbers = set()
        
        isWin = True
        for x in ln[2:]:
            if x == "|":
                isWin = False
            else:
                self.winners.add(int(x)) if isWin \
                    else self.numbers.add(int(x))
    
    def scoreCard(self):
        exp = len(self.winners.intersection(self.numbers))-1
        return 2**exp if exp >=0 else 0
    
    def countMatches(self):
        return len(self.winners.intersection(self.numbers))
    
text = AoC_ReadIn(year=23,day=4,isSample=False)
cards = dict()
for x in text:
    newCard = Card(x)
    cards[newCard.num] = newCard

# Part 1 Solution    
tot = 0
for c in cards:
    tot += cards[c].scoreCard()
    
print(tot)

# Part 2 Solution
counts = dict.fromkeys(cards,1) #Start with one of each card
for c in cards:
    for j in range(counts[c]):
        for i in range(cards[c].countMatches()):
            counts[c+i+1] += 1

tot = 0
for c in counts:
    tot += counts[c]
    
print(tot)
    
            
            
            
            
        