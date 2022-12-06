#hardcoded - ugly but working
list_of_piles = [[1],[2],[3],[4],[5],[6],[7],[8],[9]]

file = open('input.txt', 'r').readlines()

for i in range(7,-1,-1):
    for j in range(0,9):
        if file[i][1+(4*j)] != ' ':
            list_of_piles[j].append(file[i][1+(4*j)])
        else:
            pass

list_of_piles_1 = [x[:] for x in list_of_piles]
list_of_piles_2 = [x[:] for x in list_of_piles]

movement = []

for i in range(10,len(file)):
    movement.append(file[i].split('\n')[0].split('move ')[1].split(' from '))
    temp = movement[i-10][1].split(' to ')
    movement[i-10][1] = int(temp[0])
    movement[i-10].append(int(temp[1]))
    movement[i-10][0] = int(movement[i-10][0])

#part 1
for i in range(len(movement)):
    for j in range(int(movement[i][0])):
        list_of_piles_1[int(movement[i][2])-1].append(list_of_piles_1[int(movement[i][1])-1][-1])
        list_of_piles_1[int(movement[i][1])-1].pop(-1)

print(list_of_piles_1[0][-1],
      list_of_piles_1[1][-1],
      list_of_piles_1[2][-1],
      list_of_piles_1[3][-1],
      list_of_piles_1[4][-1],
      list_of_piles_1[5][-1],
      list_of_piles_1[6][-1],
      list_of_piles_1[7][-1],
      list_of_piles_1[8][-1])

#part 2     
for i in range(len(movement)):
    temp_n = movement[i][0]
    temp_f = movement[i][1]-1
    temp_t = movement[i][2]-1
    
    for j in list_of_piles_2[temp_f][-temp_n::1]:
        list_of_piles_2[temp_t].append(j)
    list_of_piles_2[temp_f] = list_of_piles_2[temp_f][0:-temp_n]
    
print(list_of_piles_2[0][-1],
      list_of_piles_2[1][-1],
      list_of_piles_2[2][-1],
      list_of_piles_2[3][-1],
      list_of_piles_2[4][-1],
      list_of_piles_2[5][-1],
      list_of_piles_2[6][-1],
      list_of_piles_2[7][-1],
      list_of_piles_2[8][-1])
