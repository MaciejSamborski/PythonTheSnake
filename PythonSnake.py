import sys
import time
import os
import msvcrt
import random
import copy
import ctypes

# Code heavily inspired by some other implementations circulating the web, but I modified it  slighty to fit my needs.
class _Cursor(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int),
                ("visible", ctypes.c_byte)]
def hide_cursor():
    cursor = _Cursor()
    handle = ctypes.windll.kernel32.GetStdHandle(-11)
    ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(cursor))
    cursor.visible = False
    ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(cursor))

# Selfdescribing consants defining gameplay.
boardWidth = 10
boardHeight = 10
snakeChar = "x"
pointChar = "o"
backgroundChar = " "
keys = ["w","s","a","d"]

class Position:
    x=0
    y=0
    def __init__(self, x=int(boardWidth/2),y=int(boardHeight/2)):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x==other.x and self.y==other.y
# Initializing some core components of game
position = Position() 
dot = Position(random.randint(0,boardWidth-1),random.randint(0,boardHeight-1))
snake = [copy.copy(position)]
random.seed()
hide_cursor()
# First static board, before actual game begins. May be replaced wih welcome screen.
for a in range(boardHeight):
        for b in range(boardWidth):
            if b==position.x and a==position.y:
                sys.stdout.write(snakeChar)
            else:
                sys.stdout.write(backgroundChar)
        sys.stdout.write("\n")
direction = msvcrt.getch().decode('utf-8')
# Main loop
while 1:
    os.system("cls")
    sys.stdout.write(str(len(snake))+"\n")
    # Printing board
    for a in range(boardHeight):
        for b in range(boardWidth):
            if Position(b,a) in snake:
                sys.stdout.write(snakeChar)
            elif b==dot.x and a==dot.y:
                sys.stdout.write(pointChar)
            else:
                sys.stdout.write(backgroundChar)
        sys.stdout.write("\n")
    # Handling user input
    if msvcrt.kbhit():
        tempDirection = msvcrt.getch().decode('utf-8')
        if tempDirection in keys:
            direction = tempDirection
    if direction == keys[0]:
        position.y=(position.y-1)%boardHeight
    elif direction == keys[1]:
        position.y=(position.y+1)%boardHeight
    elif direction == keys[2]:
        position.x=(position.x-1)%boardWidth
    elif direction == keys[3]:
        position.x=(position.x+1)%boardWidth
    if position in snake:
        break
    snake.insert(0,copy.copy(position))
    if position!=dot:
        snake.pop()
    else:
        dot = Position(random.randint(0,boardWidth-1),random.randint(0,boardHeight-1))
# Game ends
os.system("cls")
sys.stdout.write("            GAME OVER             ")
sys.stdout.flush()