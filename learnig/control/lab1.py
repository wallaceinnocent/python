import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 1. Define the Physics (RC Circuit)
R, C = 1000, 100e-6
tau = R * C
# G(s) = 1 / (tau*s + 1)
system = signal.TransferFunction([1], [tau, 1])

# 2. Create an Arbitrary Input (A Square Wave)
t = np.linspace(0, 2, 2000)
# Create a 5Hz square wave jumping between 0 and 1
u = 0.5 * (signal.square(2 * np.pi * 5 * t) + 1)

# 3. RUN THE SIMULATION
# tout = time output, yout = system response, xout = internal states
tout, yout, xout = signal.lsim(system, U=u, T=t)

# 4. Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(t, u, 'g', alpha=0.3, label='Input Signal (Square)')
plt.plot(tout, yout, 'b', linewidth=2, label='Filtered Output (Capacitor)')

plt.title("SciPy Signal Simulation: RC Low-Pass Filter")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.legend()
plt.show()