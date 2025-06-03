## python simulation of discrete SDE simulation and Approx.

import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
T = 1.0                  # Total time
N_steps = 1000            # Number of time steps
dt = T / N_steps          # Time step size
time_grid = np.linspace(0, T, N_steps + 1)

n_nests = 10              # Number of nests
sigma = 0.2               # Volatility

# Payoff parameters
b0 = 1.0                  # Baseline benefit
b_c = 2.0                 # Cooperation bonus
c_c = 0.5                 # Cooperation cost

# Fixed strategies: 5 cooperate, 5 defect
strategies = np.array([1] * 5 + [0] * 5)   # 1 = cooperate, 0 = defect

# Initialize fitness: all start at 1.0
fitness = np.ones(n_nests)

# Store fitness trajectories
fitness_trajectories = np.zeros((n_nests, N_steps + 1))
fitness_trajectories[:, 0] = fitness

# Simulation loop (Euler–Maruyama)
for n in range(N_steps):
    bar_u = np.mean(strategies)  # Average cooperation
    drift = (b0 + b_c * strategies * bar_u) - (c_c * strategies)  # Drift term for each nest
    dW = np.random.normal(0, np.sqrt(dt), size=n_nests)           # Random noise
    fitness += drift * dt + sigma * dW                            # Euler-Maruyama update
    fitness_trajectories[:, n + 1] = fitness                      # Store

# Plot fitness trajectories
plt.figure(figsize=(12, 6))
for i in range(n_nests):
    if strategies[i] == 1:
        plt.plot(time_grid, fitness_trajectories[i], label=f'Nest {i+1} (Coop)', color='blue', alpha=0.5)
    else:
        plt.plot(time_grid, fitness_trajectories[i], label=f'Nest {i+1} (Defect)', color='red', alpha=0.5)

plt.title('Fitness Trajectories of Nests (Euler-Maruyama Simulation)')
plt.xlabel('Time')
plt.ylabel('Fitness')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
