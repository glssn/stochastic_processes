import numpy as np
import time as t
# Starting cash
wealth = 200
# Print wealth
print("Starting wealth = " + str(wealth))
play = True
while (play == True):
    win = np.random.randint(2) == 1
    if wealth <= 500:
        if win == True:
            wealth = wealth * 2
            print("Current wealth: " + str(wealth))
        else:
            wealth = 0
            print("ruined")
            play = False
        t.sleep(0.2)
    else:
        if win == True:
            wealth = 1000
            print("Winner!")
            play = False
        else:
            wealth = wealth - (1000 - wealth)
        print("Current wealth: " + str(wealth))
        t.sleep(0.2)
