#Deck of Cards and their Values
#Four Houses: Spades (S), Clubs (C), Hearts (H), Diamonds (D)
#Each House has the same number of cards:
    #2=2 | 3=3 | 4=4 | 5=5 | 6=6 | 7=7 | 8=8 | 9=9 | 10=10 | King=10 | Queen=10 | Jack=10 | Ace=1/11

#Card Values
'''
1 = 1            [ ♥, ♧, ♦, ♤ ]
2 = 2            [ ♥, ♧, ♦, ♤ ]
3 = 3            [ ♥, ♧, ♦, ♤ ]
4 = 4            [ ♥, ♧, ♦, ♤ ]
5 = 5            [ ♥, ♧, ♦, ♤ ]
6 = 6            [ ♥, ♧, ♦, ♤ ]
7 = 7            [ ♥, ♧, ♦, ♤ ]
8 = 8            [ ♥, ♧, ♦, ♤ ]
9 = 9            [ ♥, ♧, ♦, ♤ ]
10 = 10          [ ♥, ♧, ♦, ♤ ]
King  = 10       [ ♥, ♧, ♦, ♤ ]
Queen = 10       [ ♥, ♧, ♦, ♤ ]
Jack = 10        [ ♥, ♧, ♦, ♤ ]
Ace = 1 or 11    [ ♥, ♧, ♦, ♤ ]
'''

from asyncore import loop
from tkinter import Variable
import random

def menu():
    input("Press Enter to Continue. . .")
    starting_menu()

def starting_menu():
    print("Choose Mode: (Press correlating key)")
    print("1] Singeplayer")
    if input(Variable)=="1":
        print("Hello")

DeckofCards = [
    "♥1","♥2","♥3","♥4","♥5","♥6","♥7","♥8","♥9","♥10","♥K","♥Q","♥J","♥A",
    "♧1","♧2","♧3","♧4","♧5","♧6","♧7","♧8","♧9","♧10","♧K","♧Q","♧J","♧A",
    "♦1","♦2","♦3","♦4","♦5","♦6","♦7","♦8","♦9","♦10","♦K","♦Q","♦J","♦A",
    "♤1","♤2","♤3","♤4","♤5","♤6","♤7","♤8","♤9","♤10","♤K","♤Q","♤J","♤A",
]

CardsValue = [
    1,2,3,4,5,6,7,8,9,10,10,10,10,1 or 11,
    1,2,3,4,5,6,7,8,9,10,10,10,10,1 or 11,
    1,2,3,4,5,6,7,8,9,10,10,10,10,1 or 11,
    1,2,3,4,5,6,7,8,9,10,10,10,10,1 or 11,
]

#Use the same code for both the player and the AI.
#AI Code:

print("Here are your cards")
for i in range(2):
    print(random.choice(DeckofCards))
    

    

    
   
