#!/usr/local/bin/python3.8

import numpy as np

def read_drawn_numbers(file):
    
    with open(file) as f:
        num = f.readline().split(',')
        return num

print(read_drawn_numbers('game_input.txt'))
    