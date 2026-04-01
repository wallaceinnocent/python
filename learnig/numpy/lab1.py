import matplotlib.pyplot as plt
import numpy as np

# --- 1. Setup ---
R = 1000       # 1k Ohm
C = 1000e-6    # 1000uF (1mF)
tau = R * C    # Time constant = 1.0s
Vs = 5.0       # 5V Source

t = np.linspace(0, 5, 500)

# --- 2. Calculate Signals ---
# Voltage: Vc(t) = Vs * (1 - e^(-t/tau))
voltage = Vs * (1 - np.exp(-t/tau))

# Current: I(t) = (Vs/R) * e^(-t/tau)
# We use Vs/R because at t=0, the capacitor is a short circuit
current = (Vs / R) * np.exp(-t/tau)

# --- 3. Plotting with Twin Axes ---
fig, ax1 = plt.subplots(figsize=(20, 9))

# Plot Voltage on the Left Axis
ax1.plot(t, voltage, 'b-', linewidth=2, label='Voltage ($V_c$)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Voltage (V)', color='b')
ax1.tick_params(axis='y', labelcolor='b')
ax1.grid(True, linestyle=':', alpha=0.5)

# Create a second Y-axis for Current (Right side)
ax2 = ax1.twinx() 

ax2.plot(t, current * 1000, 'r--', linewidth=2, label='Current ($I$)') # *1000 to show in mA
ax2.set_ylabel('Current (mA)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Adding a combined legend
fig.legend(loc="upper left", bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)

ax1.set_title("Capacitor Charging: Voltage vs Current")
plt.show()