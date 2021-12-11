#!/usr/local/bin/python3.8

import statistics as st

def get(url):
    f = open(url, 'r')
    data = []

    for x in f:
        data.append(x.strip())
    return data

data = get('aoc_input_3.txt')

def get_mode(data):
    mode = []
    for i in range(0,len(data[0])):
        tmp = []
        for x in data:
            tmp.append(x[i])
        mode.append(int(st.mode(tmp)))

    return mode

mode = get_mode(data)
print(mode)

def get_anti_mode(mode):
    anti_mode = []
    for i in range(0,len(mode)):
        if(mode[i] == 1):
            anti_mode.append(0)
        else:
            anti_mode.append(1)

    return anti_mode

anti_mode = get_anti_mode(mode)
print(anti_mode)



