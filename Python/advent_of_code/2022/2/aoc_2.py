import re

point_dict = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
    }
draw_dict = {
    'A' : 'X',
    'B' : 'Y',
    'C' : 'Z'
    }
win_dict = {
    'A' : 'Y',
    'B' : 'Z',
    'C' : 'X'
    }
lose_dict = {
    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
    }

opponent = []
player = []

with open('input_2.txt') as f:
    for line in f:
        temp = re.split(' |\n', line)
        opponent.append(temp[0])
        player.append(temp[1])
tot_score = []

for i in range(2500):
    if (
        ((opponent[i] == 'A') and (player[i] == 'Z')) or
        ((opponent[i] == 'B') and (player[i] == 'X')) or
        ((opponent[i] == 'C') and (player[i] == 'Y'))
        ):
        tot_score.append(point_dict.get(player[i]))
    if (
        ((opponent[i] == 'A') and (player[i] == 'X')) or
        ((opponent[i] == 'B') and (player[i] == 'Y')) or
        ((opponent[i] == 'C') and (player[i] == 'Z'))
        ):
        tot_score.append(point_dict.get(player[i])+3)
    if (
        ((opponent[i] == 'A') and (player[i] == 'Y')) or
        ((opponent[i] == 'B') and (player[i] == 'Z')) or
        ((opponent[i] == 'C') and (player[i] == 'X'))
        ):
        tot_score.append(point_dict.get(player[i])+6)

print(sum(tot_score))

tot_score_2 = []
for i in range(2500):
    if player[i] == 'X':
        tot_score_2.append(point_dict.get(lose_dict.get(opponent[i])))
    if player[i] == 'Y':
        tot_score_2.append(point_dict.get(draw_dict.get(opponent[i]))+3)
    if player[i] == 'Z':
        tot_score_2.append(point_dict.get(win_dict.get(opponent[i]))+6)

print(sum(tot_score_2))
