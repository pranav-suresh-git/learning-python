# Dice Simulation
 
import numpy as np

# simulate rolling 2 dice 1000 times

rolls = np.random.randint(1, 7, size=(1000,2)) #values 1 to 6
sums = np.sum(rolls, axis=1)

print("First 10 roll outcomes: \n", rolls[:10])
print("First 10 roll sums:", sums[:10])
print("Mean of all dice sums:", np.mean(sums))

