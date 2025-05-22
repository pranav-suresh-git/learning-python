#SINE Graph

import numpy as np
import matplotlib.pyplot as plt

#generate X values between the support (0, 2pi)

x = np.linspace(0, 2 * np.pi, 500)
y=np.sin(x)

#plot sine curve

plt.figure(figsize=(8,5))
plt.plot(x, y, label="sin(x)")
plt.title("Sine Curve")
plt.xlabel("x (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
