import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from astropy.time import Time
from astroquery.jplhorizons import Horizons

today = Time.now()

obj_ceres = Horizons(id='Ceres', location='@sun', epochs=today.jd)
vectors_ceres = obj_ceres.vectors()
ceres_x = vectors_ceres['x'][0]
ceres_y = vectors_ceres['y'][0]

obj_earth = Horizons(id='399', location='@sun', epochs=today.jd)
vectors_earth = obj_earth.vectors()
earth_x = vectors_earth['x'][0]
earth_y = vectors_earth['y'][0]

plt.style.use('dark_background')
plt.figure(figsize=(10, 10))

plt.scatter(0, 0, s=1000, color='yellow', label='Sun')

earth_orbit_circle = patches.Circle((0, 0), 1, edgecolor='blue', facecolor='none', linestyle='--', alpha=0.5, label="Earth's Orbit")
plt.gca().add_patch(earth_orbit_circle)

ceres_orbit_circle = patches.Circle((0, 0), 2.77, edgecolor='white', facecolor='none', linestyle='--', alpha=0.5, label="Ceres's Orbit")
plt.gca().add_patch(ceres_orbit_circle)

plt.scatter(earth_x, earth_y, s=100, color='blue', label='Earth')

plt.scatter(ceres_x, ceres_y, s=100, color='white', label='Ceres')

plt.title("Position of Ceres and Earth Relative to the Sun")
plt.xlabel("X Position (AU)")
plt.ylabel("Y Position (AU)")
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.grid(True)


plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 3.5)

plt.savefig('ceres_orbit_diagram.png') 
print("Diagram saved as ceres_orbit_diagram.png")