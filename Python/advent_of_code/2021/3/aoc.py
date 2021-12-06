import statistics as st

f = open('data_3.txt', 'r')
data = []

for x in f:
    data.append(x.strip())

mode = []
anti_mode = []

for i in range(0,len(data[1])):
    tmp = []
    for x in data:
        tmp.append(x[i])
    mode.append(int(st.mode(tmp)))

print(mode)

for i in range(0,len(mode)):
    if(mode[i] == 1):
        anti_mode.append(0)
    else:
        anti_mode.append(1)

print(anti_mode)

str_mode = ''
str_anti_mode = ''

tmp = []
for i in data:
    tmp.append(i[0])
