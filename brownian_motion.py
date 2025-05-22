#Brownian motion test code
import numpy as np
import matplotlib.pyplot as plt

'''
Brownian Motion is a random walk with 
infinitesimally small steps.
For the sake of code, you approximate by:
a cumulative sum of small Gaussian (normal) steps
'''

#parameters

T = 1.0                    # total time (1 unit)
N = 1000                   # number of steps
dt = T / N                 # small time increment dt
t = np.linspace(0, T, N)   # time grid


# Generate standard normal steps

dW = np.random.randn(N) * np.sqrt(dt)   
        #randn simulates normal increments
        #sqrt scales each step by root dt, making it time consistent

# Cumulative sum = Brownian Path 

W = np.cumsum(dW)      #gives cumulative motion, like integrating velocity

# Plot

plt.figure(figsize=(10, 5))
plt.plot(t, W, label='Brownian Path')
plt.title("Simulated Brownian Motion (1D)")
plt.xlabel("Time")
plt.ylabel("Position")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()