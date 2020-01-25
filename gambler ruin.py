import numpy as np
import time as t
import pandas as pd
import altair as alt
# pandas dataframe
df = pd.DataFrame( columns=['number of turns', 'wealth'])
# winning probability, p
p = 0.51
# losing probability, q
q = 1-p
# Starting cash
i = 10
# Print wealth
print("Starting wealth = " + str(i))
# desired wealth
W = 1000

play = True
wealth = i
turn = 0
while (play == True):
    if wealth == W:
        play = False
        print("Gambler wins!")
        break
    elif wealth == 0:
        play = False
        print("Gambler is ruined!")
        break
    turn += 1
    win = np.random.random_sample() < p
    if win == True:
        wealth += 1
    else:
        wealth -= 1
    print("Gambler now has " + str(wealth))
    df = df.append({'number of turns': turn, 'wealth': wealth}, ignore_index = True)
print(df)
