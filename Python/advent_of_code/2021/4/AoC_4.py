#!/usr/local/bin/python3.8

import numpy as np

def read_drawn_numbers(file):
    
    drawn_num = [int(num) for num in np.loadtxt(file, dtype = 'str', delimiter = ',',max_rows = 1)]
    return drawn_num
    
def read_boards(file):
    
    array = [np.loadtxt(file, skiprows=2, dtype = 'int')]
    matrices = np.reshape(array,(500, 5))
    matrices = np.vsplit(matrices, 100)
    return matrices
    
#print(read_drawn_numbers('../4/game_input.txt'))
#print(read_boards('../4/game_input.txt'))

def main():
    
    #Load data
    drawn = read_drawn_numbers('../4/game_input.txt')
    mat = read_boards('../4/game_input.txt')
    
    #Initiate empty array for drawn numbers
    tmp = []
    run = True
    ite = 0
    
    
    while run:
        for i in range(0,len(drawn)):  
            tmp.append(drawn[i])  
            for matrix in mat:
                if sum(np.isin(matrix[1,:],tmp)) == 5:
                    
                    run = False
                    break
            ite += 1
            
    print(ite)
    
main()