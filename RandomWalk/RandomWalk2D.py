import numpy as np
import matplotlib.pyplot as plt

# Paramètres de la simulation
num_steps = 1000  # Nombre d'étapes
step_size = 1  # Taille d'une étape
x = 0
y = 0


for i in range(3):
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
    print(z)

