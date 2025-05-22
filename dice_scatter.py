#dice scatter

import numpy as np
import matplotlib.pyplot as plt

##simulate 1000 rolls of two dice

rolls = np.random.randint(1, 7, size=(1000, 2))
die1 = rolls [:, 0]
die2 = rolls [:, 1]

#Scatter plot: each point = one roll

plt.figure(figsize=(6,6))             #creates the canvas (6x6 inches)
plt.scatter(die1, die2, alpha=0.5)    #draws the data
plt.title("Scatter of dice rolls")    #adds title
plt.xlabel("Die 1")                   #adds label
plt.ylabel("Die 2")
plt.grid(True)                        #adds gridlines
plt.tight_layout()                    #optimizes spacing to fit
plt.show()                            #renders and displays figure