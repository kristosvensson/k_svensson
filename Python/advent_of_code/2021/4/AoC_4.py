#!/usr/local/bin/python3.8

import numpy as np

def read_drawn_numbers(file):
    
    drawn_num = [int(num) for num in np.loadtxt(file, dtype = 'str', delimiter = ',',max_rows = 1)]
    return drawn_num
    
def read_matrices(file, i):
    
    array = [np.loadtxt(file, skiprows=2, dtype = 'int')]
    matrices = np.reshape(array,(i,5))
    matrices = np.vsplit(matrices, 100)
    return matrices
    
print(read_drawn_numbers('../4/game_input.txt'))

mat = read_matrices('../4/game_input.txt',500)

for array in mat:
    print(array[:,3])


a =[1,2,3]
b = [5,4,3,2,1]

a=b