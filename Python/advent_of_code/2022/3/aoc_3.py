class Rucksack:
    def __init__(self, allez, comp1, comp2):
        self.allez = allez
        self.comp1 = comp1
        self.comp2 = comp2

rucksacks = []

with open('input.txt') as file:
    for line in file:
        rucksacks.append(Rucksack(line,line[0:int(len(line)/2)],line[int(len(line)/2):int(len(line))]))

list_inv = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I',
            'J','K','L','M','N','O','P','Q','R',
            'S','T','U','V','W','X','Y','Z']

sum_prio = []

for i in rucksacks:
    for j in i.comp1:
        if j in i.comp2:
            sum_prio.append(list_inv.index(j)+1)
            break

print(sum(sum_prio))

sum_prio3 = []

for i in range(0,len(rucksacks),3):
    for j in rucksacks[i].allez:
        if (j in rucksacks[i+1].allez) and (j in rucksacks[i+2].allez):
            sum_prio3.append(list_inv.index(j)+1)
            break
            
print(sum(sum_prio3))
