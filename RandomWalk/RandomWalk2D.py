import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la simulation
num_steps = 1000  # Nombre d'étapes
step_size = 1  # Taille d'une étape
x = 0
y = 0
x_coords = [x]
y_coords = [y]

np.random.seed(5)

for i in range(num_steps):
    p = np.random.randint(0, 4)
    print(p)
    
    if p == 0:
        x = x + step_size
    elif p == 1:
        x = x - step_size
    elif p == 2:
        y = y + step_size
    elif p == 3:
        y = y - step_size
    z = (x, y)
    x_coords.append(x)
    y_coords.append(y)

print(x,y)

plt.figure(figsize=(12,8))
plt.plot(x_coords, y_coords, marker='o', linestyle='-')
plt.plot(0,0, marker= 'o', c='r')
plt.plot(x,y, marker='o', c='black')
plt.grid(ls='--')
plt.show()

#Test