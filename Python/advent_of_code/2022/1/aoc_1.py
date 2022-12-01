temp = []
temp_sum = 0
with open('input.txt') as f:
    for line in f:
        if line != '\n':
            temp_sum += int(line)
        elif line == '\n':
            temp.append(int(temp_sum))
            temp_sum = 0
        else:
            break
    temp.append(temp_sum)
temp.sort(reverse = True)
print(temp[0])
print(sum(temp[0:3]))
