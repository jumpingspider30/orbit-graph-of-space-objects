# Import the necessary libraries
import os
import matplotlib.pyplot as plt
import numpy as np
from astropy.time import Time
from astroquery.jplhorizons import Horizons

# 1. Get today's date and time
today = Time.now()

# 2. Get the location of Europa using JPL Horizons (NAIF ID 502)
obj_europa = Horizons(id='502', location='@sun', epochs=today.jd)
vectors_europa = obj_europa.vectors()
europa_x = vectors_europa['x'][0]
europa_y = vectors_europa['y'][0]

# 3. Get the location of Earth using JPL Horizons
obj_earth = Horizons(id='399', location='@sun', epochs=today.jd)
vectors_earth = obj_earth.vectors()
earth_x = vectors_earth['x'][0]
earth_y = vectors_earth['y'][0]

# 4. Create the plot
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the Sun at the center
ax.scatter(0, 0, s=1200, color='gold', edgecolor='orange', linewidth=2, zorder=3, label='Sun')

# ----------------- BEAUTIFIED ORBITS -----------------
theta = np.linspace(0, 2*np.pi, 500)

# Earth's orbit (1 AU)
ax.plot(np.cos(theta), np.sin(theta), '--', color='deepskyblue', alpha=0.6, linewidth=1.5, label="Earth's Orbit")

# Europa's orbit (~5.2 AU, same as Jupiter)
ax.plot(5.2*np.cos(theta), 5.2*np.sin(theta), '--', color='white', alpha=0.6, linewidth=1.5, label="Europa's Orbit (≈ Jupiter)")
# ----------------- END ORBITS -----------------

# Plot Earth
ax.scatter(earth_x, earth_y, s=180, color='deepskyblue', edgecolor='white', linewidth=1.5, zorder=4, label='Earth')
ax.text(earth_x+0.1, earth_y+0.1, 'Earth', fontsize=10, color='deepskyblue')

# Plot Europa
ax.scatter(europa_x, europa_y, s=180, color='white', edgecolor='gray', linewidth=1.5, zorder=4, label='Europa')
ax.text(europa_x+0.1, europa_y+0.1, 'Europa', fontsize=10, color='white')

# ----------------- STYLING -----------------
ax.set_title("Europa and Earth Relative to the Sun", fontsize=16, color='w', pad=20)
ax.set_xlabel("X Position (AU)", fontsize=12)
ax.set_ylabel("Y Position (AU)", fontsize=12)


# Axis limits
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal', adjustable='box')

# Light grid
ax.grid(color='gray', linestyle=':', linewidth=0.5, alpha=0.5)

# Save the figure
plt.savefig(os.path.join('europa_solar_system_diagram.png'), dpi=300, bbox_inches='tight')
print("Diagram saved as europa_solar_system_diagram.png")

