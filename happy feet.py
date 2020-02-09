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
            print("bet is won")
            wealth = wealth * 2
            print("Current wealth: " + str(wealth))
        else:
            print("bet is lost")
            wealth = 0
            print("ruined")
            play = False
        t.sleep(0.2)
    else:
        if win == True:
            wealth = 1000
            print("bet is won")
            print("Winner!")
            play = False
        else:
            print("bet is lost")
            stake = 1000 - wealth
            wealth = wealth - stake
        print("Current wealth: " + str(wealth))
        t.sleep(0.2)
