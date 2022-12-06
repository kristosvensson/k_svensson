with open('input.txt') as f:
    for line in f:
        string = line
def day_5(x):
    for i in range(len(string)):
        if i >= x-1:
            temp = string[i:i-x:-1]
            unique = []
            for j in temp:
                if j not in unique:
                    unique.append(j)
                else:
                    pass
            if len(unique) == x:
                print(i+1, temp[::-1])
                break
#part one
day_5(4)
#part two
day_5(14)
