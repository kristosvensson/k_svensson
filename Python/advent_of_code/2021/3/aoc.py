#!/usr/local/bin/python3.8

import numpy as np

def get(url):
    f = open(url, 'r')
    data = []

    for x in f:
        data.append(x.strip())
    return data

def get_mode_i(data, i):
    tmp = []
    
    for x in data:
        tmp.append(int(x[i]))
    if np.mean(tmp) >= 0.5:
        return 1
    else:
        return 0

def get_anti_mode_i(data, i):
    tmp = []
    for x in data:
        tmp.append(int(x[i]))    
    if np.mean(tmp) < 0.5:
        return 1
    else:
        return 0
        
def get_mode(data):
    mode = []
    for i in range(0,len(data[0])):
        tmp = []
        for x in data:
            tmp.append(int(x[i]))
        if np.mean(tmp) >= 0.5:
            mode_tmp = 1
        else:
            mode_tmp = 0
        mode.append(mode_tmp)

    return mode

def get_anti_mode(mode):
    anti_mode = []
    for i in range(0,len(mode)):
        if(mode[i] == 1):
            anti_mode.append(0)
        else:
            anti_mode.append(1)

    return anti_mode

def calc_bin(data):
    num = 0
    for i in range(0,len(data)):
            num += (data[-(i+1)]) * 2 ** i
    return num

def filter_i(data, i, num):
    tmp_data = []
    for x in data:
        if int(x[i]) == num:
            tmp_data.append(x)
    return tmp_data
    
def find_oxy(data):
    tmp_filter = filter_i(data, 0, get_mode_i(data, 0))
    for i in range(1,len(data[0])):
        if len(tmp_filter) == 1:
            break
        else:
            tmp_filter = filter_i(tmp_filter, i, get_mode_i(tmp_filter, i))
    tmp = []
    for i in range(0,len(tmp_filter[0])):
        tmp.append(int(tmp_filter[0][i]))
    return tmp

def find_co(data):
    tmp_filter = filter_i(data, 0, get_anti_mode_i(data, 0))
    for i in range(1,len(data[0])):
        if len(tmp_filter) == 1:
            break
        else:
            tmp_filter = filter_i(tmp_filter, i, get_anti_mode_i(tmp_filter, i))
    tmp = []
    for i in range(0,len(tmp_filter[0])):
        tmp.append(int(tmp_filter[0][i]))
    return tmp

def main():
    data = get('aoc_input_3.txt')
    mode = get_mode(data)
    anti_mode = get_anti_mode(mode)
    print("Power consumption:",calc_bin(mode)*calc_bin(anti_mode))    
    oxy = find_oxy(data)
    co = find_co(data)
    print("Oxygen generator rating:", calc_bin(oxy))
    print("CO2 scrubber rating:", calc_bin(co))
    print("Life support rating:", calc_bin(oxy)*calc_bin(co))
    
    
main()