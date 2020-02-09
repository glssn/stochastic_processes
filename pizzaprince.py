import numpy as np
import pandas as pd
import altair as alt

# Starting variables
gamma = 0.2
days = 0.1
howlong = 5000

# Setup
today = 0
pocketmoney = 0
moneylist = [None] * howlong
daylist = list(range(howlong))

while(today<howlong):
    if pocketmoney == 0:
        pocketmoney = pocketmoney + np.random.geometric(gamma)
    pizzaday = np.random.geometric(days)
    i = 0
    if (today + pizzaday <= howlong):
        while(i < pizzaday):
            moneylist[today + i] = pocketmoney
            i = i + 1
        today = today + pizzaday
        pocketmoney = pocketmoney - 1
        moneylist[today] = pocketmoney
    else:
        daysleft = howlong - today
        while(i < daysleft):
            moneylist[today + i] = pocketmoney
            i = i + 1
        today = howlong

# visualisation
df = pd.DataFrame()
df['days'] = daylist
df['money'] = moneylist
alt.Chart(df).mark_line(interpolate='step-after').encode(
    x='days',
    y='money'
)
