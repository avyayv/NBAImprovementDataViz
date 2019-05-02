import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Name", "Score"]

plt.ylim(-20, 15)

players = json.loads(open('final_with_season.json').read())

dict = {}
actual_number = {}

total_dict = {}
number_dict = {}

STAT = 'PTS'

highlighted_players = ['Gordon Hayward']

for player in players:
    for index, base in enumerate(player['nice_dict']['Base']):
        if index == 0:
            dict[player['name']] = [0]
            actual_number[player['name']] = [0]
        elif('Usage' in player['nice_dict'] and player['nice_dict']['Usage'][index]['USG_PCT'] > 0 and player['nice_dict']['Usage'][0]['USG_PCT'] > 0):
            dict[player['name']].append(base[STAT]*0.2/player['nice_dict']['Usage'][index]['USG_PCT']*24/base['MIN']-player['nice_dict']['Base'][0][STAT]*0.2/player['nice_dict']['Usage'][0]['USG_PCT']*24/base['MIN'])
            actual_number[player['name']].append(base[STAT])

x.sortby = "Score"

good_indices = []
good_values = []


for index, key in enumerate(dict.keys()):

    if key in highlighted_players:
        good_indices.append([i for i in range(1, len(dict[key])+1)])
        good_values.append(dict[key])


    if max(actual_number[key]) > 15:
        if(min(dict[key]) < -20):
            print(key)

        plt.plot([i for i in range(1, len(dict[key])+1)], dict[key], color='0.9')

        for i in range(1, len(dict[key])+1):
            if i in total_dict and i < 19:
                total_dict[i] += dict[key][i-1]
            elif i < 19:
                total_dict[i] = dict[key][i-1]

            if i in number_dict and i < 19:
                number_dict[i] += 1
            elif i < 19:
                number_dict[i] = 1

    plt.ylabel('Marginal Points')

for key in total_dict.keys():
    total_dict[key] = total_dict[key]/number_dict[key]


plt.plot([i for i in total_dict.keys()], [total_dict[key] for key in total_dict.keys()], color='0.0')

for index, good_index in enumerate(good_indices):
    plt.plot(good_index, good_values[index], color='blue')

plt.show()

(['6%2B+Feet+-+Wide+Open', '4-6+Feet+-+Open', '2-4+Feet+-+Tight', '0-2+Feet+-+Very+Tight', 'Drives',
'Defense', 'CatchShoot', 'Passing', 'SpeedDistance', 'Rebounding',
'Possessions', 'PullUpShot', 'ElbowTouch', 'PostTouch',
'PaintTouch', 'Efficiency', 'Touch+<+2+Seconds', 'Touch+2-6+Seconds',
'Touch%206%2B%20Seconds', '0%20Dribbles', '1%20Dribble', '2%20Dribbles',
'3-6%20Dribbles', '7%2B%20Dribbles', '24-22', '22-18%20Very%20Early',
'18-15%20Early', '15-7%20Average', '7-4%20Late', '4-0%20Very%20Late',
'Base', 'Advanced', 'Misc', 'Scoring', 'Usage'])
