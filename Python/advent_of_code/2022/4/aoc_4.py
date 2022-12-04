input = []
with open('input.txt') as file:
    for line in file:
        input.append([
            list(range(int(line.split('\n')[0].split(',')[0].split('-')[0]),(int(line.split('\n')[0].split(',')[0].split('-')[1])+1))),
            list(range(int(line.split('\n')[0].split(',')[1].split('-')[0]),(int(line.split('\n')[0].split(',')[1].split('-')[1])+1)))
            ])
total_overlap,overlap = 0,0
for line in input:
    if ((line[0][0] >= line[1][0]) and (line[0][-1] <= line[1][-1]) or (line[1][0] >= line[0][0]) and (line[1][-1] <= line[0][-1])):
        total_overlap += 1
    if ((line[0][0] >= line[1][0]) and (line[0][0] <= line[1][-1]) or (line[1][0] >= line[0][0]) and (line[1][0] <= line[0][-1])):
        overlap += 1
print('Helt överlappande:',total_overlap,'\nDelvis överlappande:',overlap)
