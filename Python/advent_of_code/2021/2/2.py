#!/usr/local/bin/python3.8

import numpy as np

file = open("advent_of_code_input_2.txt", "r")

data = file.read().splitlines()

file.close()

class submarine:
    def __init__(self, pos_x, pos_z, aim):
            self.pos_x = 0
            self.depth = 0
            self.aim = 0
            
sub = submarine(0,0,0)

tmp = []

for x in data:
    tmp = x.split(" ")
    if (tmp[0] == 'forward'):
        sub.pos_x = sub.pos_x + int(tmp[1])
        sub.depth = sub.depth + sub.aim * int(tmp[1])
    elif (tmp[0] == 'up'):
        sub.aim = sub.aim - int(tmp[1])
    elif (tmp[0] == 'down'):
        sub.aim = sub.aim + int(tmp[1])
        
print("Final X position: ", sub.pos_x,"\n\nFinal depth: ", sub.depth,"\n\nFinal X position multiplied with final depth: ", sub.pos_x * sub.depth)