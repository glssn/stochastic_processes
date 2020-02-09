import numpy as np
import time as t
import pandas as pd
import altair as alt
# pandas dataframe
df = pd.DataFrame( columns=['number of turns', 'wealth'])
# winning probability, p
p = 0.6
# losing probability, q
q = 1-p
# Starting cash
i = 100
prints = False
# Print wealth
print("Starting wealth = £" + str(i))
# desired wealth
W = 1000
print("Goal wealth = £" + str(W))

play = True
wealth = i
turn = 0

while (play == True):
    if wealth == W:
        play = False
        if prints == True:
            print("Gambler wins!")
        break
    elif wealth == 0:
        play = False
        if prints == True:
            print("Gambler is ruined!")
        break
    turn += 1
    win = np.random.random_sample() < p
    if win == True:
        wealth += 1
    else:
        wealth -= 1
    if prints == True:
        print("Gambler now has " + str(wealth))
    df = df.append({'number of turns': turn, 'wealth': wealth}, ignore_index = True)

alt.Chart(df).mark_line(interpolate='step-after').encode(
    x='number of turns',
    y='wealth',
    tooltip='wealth'
)
